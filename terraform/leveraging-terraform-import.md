# Leveraging Terraform Import

[[_TOC_]]

## Introduction

Terraform provides the [import][1] command to import existing resources, but there are a few things that needs to be taken in consideration to ensure our Terraform code becomes a true representation of the infrastructure.

## Basics of resource importing

    Consider managing an existent GCP project

Following Terraform's examples, you might try something like this:

1. Create a resource block matching the type of the object to be imported, in this case, `google_project`:

    ```hcl
    # main.tf

    resource "google_project" "default" {}
    ```

2. Run `terraform init` command to download the necessary google provider plugin:

    ```bash
    terraform init
    ```

3. Run the `terraform import` command using the proper `google_project` [import syntax][2]:

    ```bash
    terraform import google_prject.default my-project
    ```

    We can then verify that the project has been imported by running:

    ```bash
    terraform state show google_project.default
    ```

    Output:

    ```bash
    # google_project.default:
    resource "google_project" "default" {
        auto_create_network = true
        folder_id           = "000000000000"
        id                  = "projects/my-project"
        labels              = {
            "env"             = "dev"
        }
        name                = "my-project"
        number              = "000000000000"
        project_id          = "my-project"

        timeouts {}
    }
    ```

This seems to work well enough until you decide you need to make changes to that resource.

## Updating an imported resource

Let's try adding a new project label by editing our previous code:

```hcl
# main.tf

resource "google_project" "default" {
    labels = {
        "test" = "new-label"
    }
}
```

Running `terraform plan`:

```bash
$ terraform plan

Error: Missing required argument

  on main.tf line 1, in resource "google_project" "default":
   1: resource "google_project" "default" {

The argument "project_id" is required, but no definition was found.


Error: Missing required argument

  on main.tf line 1, in resource "google_project" "default":
   1: resource "google_project" "default" {

The argument "name" is required, but no definition was found.
```

It should come as no surprise that just specifying the new label inside our empty resource block is not enough. The arguments `project_id` and `name` are required:

```hcl
# main.tf

resource "google_project" "default" {
  project_id = "my-project"
  name       = "my-project"
  labels = {
    "test" = "new-label"
  }
}

```

Running `terraform plan`:

```bash
$ terraform plan
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.

google_project.default: Refreshing state... [id=projects/my-project]

------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # google_project.default will be updated in-place
  ~ resource "google_project" "default" {
        auto_create_network = true
        folder_id           = "000000000000"
        id                  = "projects/my-project"
      ~ labels              = {
          - "env"             = "dev" -> null
          + "test"            = "new-label"
        }
        name                = "my-project"
        number              = "000000000000"
        project_id          = "my-project"

        timeouts {}
    }

Plan: 0 to add, 1 to change, 0 to destroy.
```

This looks better, but the plan is showing that all other labels will be replaced, so we need to remap all the current labels as well:

```hcl
# main.tf

resource "google_project" "default" {
  project_id = "my-project"
  name       = "my-project"
  labels = {
    "env"             = "dev"
    "test"            = "new-label"
  }
}

```

Running `terraform plan`:

```bash
$ terraform plan
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.

google_project.default: Refreshing state... [id=projects/my-project]

------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # google_project.default will be updated in-place
  ~ resource "google_project" "default" {
        auto_create_network = true
        folder_id           = "000000000000"
        id                  = "projects/my-project"
      ~ labels              = {
            "env"             = "dev"
          + "test"            = "new-label"
        }
        name                = "my-project"
        number              = "000000000000"
        project_id          = "my-project"

        timeouts {}
    }

Plan: 0 to add, 1 to change, 0 to destroy.
```

Good. We finally managed to specify enough of the resource to the point that the only update to the object is the addition of a new label called `test`.

## Working with more extensive infrastructures

Even if no change to the resource was required, if we just kept our empty resource specification as we first defined (which was all it took to be able to import the project), our source code would be far from representing our actual infrastructure.

Now imagine importing resources like a GKE cluster, or hundreds of IAM policy bindings.
Let's go back to the example of importing a GCP project and see what improvements we can make.

### Importing the resource

Instead of writing an empty resource to `main.tf` and then running the import command, let's import the project to our terraform state directly:

```bash
# We need to define provider and initialize terraform before running the import command
printf 'provider "google" {}\n\n' > main.tf
terraform init
terraform import -allow-missing-config google_project.default my-project
```

The `-allow-missing-config` flag allows importing the project without creating the `google_project.default` resource block.

Here is another way to find out the resource import format:

```bash
$ tfis google_project
==> google_project
Documentation URL: https://www.terraform.io/docs/providers/google/r/google_project.html
Import formats:
terraform import google_project.my_project your-project-id
```

[tfis][7] is a little tool that scrapes Terraform documentation looking for the import syntax of a given resource.

### Writing the resource code

Now write the resource code, but instead of doing it manually, let's generate it using the `terraform state show` command:

```bash
terraform state show -no-color google_project.default >> main.tf
```

The `-no-color` prevents any color formatting characters from creeping into our code.

Current `main.tf` content:

```terraform
provider "google" {}

# google_project.default:
resource "google_project" "default" {
    auto_create_network = true
    folder_id           = "000000000000"
    id                  = "projects/my-project"
    labels              = {
        "ac-number"       = "us106088"
        "env"             = "dev"
        "financial-owner" = "smohan3"
        "slb-org"         = "sdfc"
        "ssr"             = "ear-aa-7542"
        "technical-owner" = "kiehn1"
    }
    name                = "my-project"
    number              = "000000000000"
    project_id          = "my-project"

    timeouts {}
}
```

Not bad, but what do we get if we run `terraform plan` now?

```bash
$ terraform plan

Error: "number": this field cannot be set

on main.tf line 4, in resource "google_project" "default":
4: resource "google_project" "default" {



Error: : invalid or unknown key: id

on main.tf line 4, in resource "google_project" "default":
4: resource "google_project" "default" {
```

We get an error because `number` and `id` are not valid fields. They are [computed attributes][6] of the resource. Remove those fields should fix our code and running the `plan` again should show no changes to our infrastructure:

```bash
$ terraform plan
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.

google_project.default: Refreshing state... [id=projects/my-project]

------------------------------------------------------------------------

No changes. Infrastructure is up-to-date.

This means that Terraform did not detect any differences between your
configuration and real physical resources that exist. As a result, no
actions need to be performed.
```

### tfschema tool

To find out all the computed attributes for a particular resource, use the [tfschema][4] tool, a schema inspector for Terraform providers:

```bash
$ tfschema resource show google_project
+---------------------+-------------+----------+----------+----------+-----------+
| ATTRIBUTE           | TYPE        | REQUIRED | OPTIONAL | COMPUTED | SENSITIVE |
+---------------------+-------------+----------+----------+----------+-----------+
| auto_create_network | bool        | false    | true     | false    | false     |
| billing_account     | string      | false    | true     | false    | false     |
| folder_id           | string      | false    | true     | true     | false     |
| id                  | string      | false    | true     | true     | false     |
| labels              | map(string) | false    | true     | false    | false     |
| name                | string      | true     | false    | false    | false     |
| number              | string      | false    | false    | true     | false     |
| org_id              | string      | false    | true     | true     | false     |
| project_id          | string      | true     | false    | false    | false     |
| skip_delete         | bool        | false    | true     | true     | false     |
+---------------------+-------------+----------+----------+----------+-----------+

block_type: timeouts, nesting: NestingSingle, min_items: 0, max_items: 0
+-----------+--------+----------+----------+----------+-----------+
| ATTRIBUTE | TYPE   | REQUIRED | OPTIONAL | COMPUTED | SENSITIVE |
+-----------+--------+----------+----------+----------+-----------+
| create    | string | false    | true     | false    | false     |
| delete    | string | false    | true     | false    | false     |
| read      | string | false    | true     | false    | false     |
| update    | string | false    | true     | false    | false     |
+-----------+--------+----------+----------+----------+-----------+
```

Or better yet, if you have something like [jq][5] we can get just the computed attributes:

```bash
$ tfschema resource show -format=json google_project | jq '.attributes[] | select( .computed == true) | .name'
"folder_id"
"id"
"number"
"org_id"
"skip_delete"
```

---
[1]: https://www.terraform.io/docs/import/index.html
[2]: https://www.terraform.io/docs/providers/google/r/google_project.html#import
[3]: https://github.com/minamijoyo/tfschema/releases
[4]: https://github.com/minamijoyo/tfschema
[5]: https://stedolan.github.io/jq/
[6]: https://www.terraform.io/docs/providers/google/r/google_project.html#attributes-reference
[7]: https://github.com/wils0ns/tfis
