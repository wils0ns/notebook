# Terraform State Management

[[_TOC_]]

## Remote state

Terraform [remote state][1] using [GCS backend][2] is LightOps current storage of choice.

Advantages:

* [Collaboration][5] - Allows teams to collaborate and share the state of infrastructure resources
* [State locking][3] - This prevents others from acquiring the lock and potentially corrupting your state
* [State versioning][4] - By enabling Object versioning on the GCS bucket

## Single state Pattern

This pattern provides the simplest way to maintain your infrastructure and it can be used as its single source of truth.

Code structure example:

```bash
wiki/Terraform/single-state-example/
├── main.tf
├── project.tf
├── iam.tf
├── outputs.tf
└── variables.tf
```

Collaborating with others is manageable thanks to [state locking](https://www.terraform.io/docs/state/locking.html),
but conflicting changes to the same managed resources can still be an issue.

## Multiple state Pattern

Using this pattern can help control team permissions within the managed infrastructure. Service accounts with specific roles can be assigned to different teams and with those constraints, it would make no sense having teams with different privileges managing the same resource group. Separate states can help make that boundary more explicit.

Code structure example:

```bash
wiki/Terraform/multi-state-example/
├── iam
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
└── project
    ├── main.tf
    ├── outputs.tf
    └── variables.tf
```

Make use of Terraform [remote_state][6] data source to have access to the outputs of other remote state files.

## Moving/renaming state resources

As the managed infrastructure matures, also does the code that specifies it.
Renaming resources to be more meaningful, more descriptive, or moving resources across state boundaries for a more logical organization.

In Terraform, renaming a managed resource means destroying the current object and creating a new one. To avoid this, make use of [terraform state mv][7] command.

## Importing unmanaged resources

The simplest way of Adopting Terraform on existent infrastructure is to simply destroy the objects and reconstruct them using [Terraform resources][8], but sometimes, redeploying resources can mean service downtime, which might not be an option on production environments.

Although Terraform provides the [import][9] command as a way to import existing infrastructure, it is far from practical. So we wrote an article demonstrating ways to [leverage terraform import](leveraging-terraform-import.md).

---
[1]: https://www.terraform.io/docs/state/remote.html
[2]: https://www.terraform.io/docs/backends/types/gcs.html
[3]: https://www.terraform.io/docs/state/locking.html
[4]: https://cloud.google.com/storage/docs/object-versioning
[5]: https://www.terraform.io/docs/state/remote.html#delegation-and-teamwork
[6]: https://www.terraform.io/docs/providers/terraform/d/remote_state.html
[7]: https://www.terraform.io/docs/commands/state/mv.html
[8]: https://www.terraform.io/docs/configuration/resources.html
[9]: https://www.terraform.io/docs/import/index.html
