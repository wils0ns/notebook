# Terraform

## Installation

On Linux, install `wget` and `unzip` and run the following commands:

```bash
TERRAFORM_VERSION=0.13.4
cd /tmp
wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin
```

For other platforms, check out Terraform's [download][tf-download] page.

## What next?

Curated material regarding Terraform practices, patterns, and third-party resources.

* [Best Practices](best-practices.md) - Best practices for consistent infrastructure and team collaboration.
* [State Management](state-management.md) - Strategies on managing new and existent infrastructure resources.
* [Leveraging Terraform Import](leveraging-terraform-import.md) - Some insight on working with existent resources not initially managed by your Terraform state
* [Resources](resources.md) - Collection of third-party resources.


[tf-download]: https://www.terraform.io/downloads.html
