provider "aws" {
  region = "ap-south-1"
}

# Security Group
resource "aws_security_group" "sustainability_sg" {
  name        = "sustainability_sg"
  description = "Allow HTTP and SSH"
  vpc_id      = "vpc-0a62d6d5f3f1bc689" # replace with your VPC ID if different

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "sustainability_app" {
  ami           = "ami-0317b0f0a0144b137" # Amazon Linux 2023, Mumbai
  instance_type = "t3.micro"
  key_name      = "sustainability_key"
  vpc_security_group_ids = [aws_security_group.sustainability_sg.id]

  instance_market_options {
    market_type = "spot"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              systemctl start docker
              systemctl enable docker

              docker pull nidhan7/sustainability-app:latest
              docker run -d -p 80:8000 --name sustainability-app nidhan7/sustainability-app:latest
              EOF

  tags = {
    Name = "SustainabilityApp"
  }
}

output "instance_ip" {
  value = aws_instance.sustainability_app.public_ip
}
