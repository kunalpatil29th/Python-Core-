# terraform_hcl_sim.py

"""
Definition: Terraform is an open-source infrastructure as code (IaC) software tool that provides a consistent CLI workflow to manage hundreds of cloud services.
"""

def terraform_apply():
    hcl_config = """
    resource "aws_instance" "app_server" {
      ami           = "ami-0c55b159cbfafe1f0"
      instance_type = "t2.micro"
    }
    """
    print("Terraform Plan: 1 to add, 0 to change, 0 to destroy.")
    print("Applying changes...")
    print("Creation complete after 30s.")

terraform_apply()
