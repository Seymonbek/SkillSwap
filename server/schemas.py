from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class ReputationSchema(Schema):
    user_id = fields.Int(required=True)
    score = fields.Int(required=True)

class SkillSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    level = fields.Int(required=True)

class SessionSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    timestamp = fields.DateTime(required=True)

class JobSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    user_id = fields.Int(required=True)