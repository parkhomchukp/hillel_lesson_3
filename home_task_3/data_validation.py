from marshmallow import validate
from webargs import fields

password_args = {
    "length": fields.Int(
        # required=True,
        missing=10,
        validate=[validate.Range(min=1, max=999)],
    ),
    "specials": fields.Int(
        missing=0,
        validate=[validate.Range(min=0, max=1)],
    ),
    "digits": fields.Int(
        missing=0,
        validate=[validate.Range(min=0, max=1)],
    )
}
