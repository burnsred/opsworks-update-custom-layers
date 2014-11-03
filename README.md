# opsworks-update-custom-layers

Updates custom cookbooks and runs all custom deploy recipes for each layer.

Requires the following environmental variables to be set

 * `AWS_ACCESS_KEY_ID`: an AWS access key;
 * `AWS_SECRET_ACCESS_KEY`: the secret key for the above account.

Call as

    opsworks-update-custom-layers --stack-id <stack_id> --comment <comment_for_deployment>
