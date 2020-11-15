---
toc: true
---
# Terraform Best practices

## The master branch of the infrastructure repository should be a 1:1 representation of what’s actually deployed in production

Once you start using Terraform, do not make changes via a web UI, or manual API calls, or any other mechanism. Running `terraform apply` against the production environment should only be done from the master branch.

## Do not use Terraform Environments/Workspaces

If you use workspaces, your infrastructure repo will only have one copy of the code, even though you may have several environments deployed with it. From merely looking at the code, there will be no way to know what’s actually deployed.

## For any shared environment, always deploy from a single branch

Branching and Terraform are a bad combination. Terraform is implicitly a mapping from Terraform code to infrastructure deployed in the real world. Since there’s only one real world, it doesn’t make much sense to have multiple branches of your Terraform code. So for any shared environment (e.g., stage, prod), always deploy from a single branch.

## Deployment strategies

Errors are fairly common with Terraform. Therefore, your deployment strategy should assume errors are (relatively) normal and offer a first-class way to deal with them:

* **Retries**: Certain types of Terraform errors are transient, and go away if you re-run `terraform apply`. The deployment tooling you use with Terraform should detect these known errors and automatically retry after a brief pause

* **Terraform state errors**: Occasionally, Terraform will fail to save state after running `terraform apply`. For example, if you lose Internet connectivity part way through an `apply`, not only will the `apply` fail, but Terraform won’t be able to write the updated state file to your remote backend. In these cases, Terraform will save the state file on disk in a file called `errored.tfstate`. Make sure that your CI server does not delete these files (e.g., as part of cleaning up the workspace after a build). If you can still access this file after a failed deployment, once Internet connectivity is restored, you can push this file to your remote backend using the `terraform state push` command
so that the state information isn’t lost.

* **Errors releasing locks**: Occasionally, Terraform will fail to release a lock. For example, if your CI server crashes in the middle of a `terraform apply`, the state will remain permanently locked. Anyone else who tries to run `apply` on the same module will get an error message saying the state is locked, and the ID of the lock. If you’re absolutely sure this is an accidentally left-over lock, you can forcibly release it using the `terraform force-unlock` command, passing it the ID of the lock from that error message.

## References

* [Terraform: Up & Running, 2nd Edition](https://blog.gruntwork.io/terraform-up-running-2nd-edition-early-release-is-now-available-b104fc29783f)
