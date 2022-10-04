# test-secrets

This project contains an sample Lambda function to read a environment variable from local or from AWS Parameters
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html

 It includes the following files and folders.

- lambda_app - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.


## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

Test a single function by invoking it directly with a local parameters. Local parameters should be included in the `environment_variables.json` file

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke -n environment_variables.json
```

## Resources

I have found usefull the following video https://www.youtube.com/watch?v=fL3ToMdoXDw
