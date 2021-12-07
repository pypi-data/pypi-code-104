from aws_cdk import (
    aws_secretsmanager,
    core
)


class SecretGenerator(core.Construct):
    def __init__(self, scope: core.Construct, id: str, secret_name: str, template: str = None, key: str = None) -> None:
        """Provides a generate pseudo-random password

        Args:
            scope (core.Construct): [description]
            id (str): [description]
            secret_name (str): [description]
            template (str, optional): [description]. Defaults to None.
            key (str, optional): [description]. Defaults to None.
        """
        super().__init__(scope, id)
        self.secret = aws_secretsmanager.Secret(
            self,
            id,
            generate_secret_string=aws_secretsmanager.SecretStringGenerator(
                secret_string_template=template,
                generate_string_key=key,
                password_length=24,
                exclude_characters='"@/\$'
            ),
            secret_name=secret_name
        )

    def to_string(self):
        return core.SecretValue(self.secret.secret_value.to_string())
