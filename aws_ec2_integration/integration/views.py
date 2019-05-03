from django.shortcuts import render
import boto3


def index(request):
    ec2 = boto3.client('ec2')
    resp = ec2.describe_instances()
    return render(request, 'test.html', {'context': resp})
