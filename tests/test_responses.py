from Portfolio_Project.User_Responses import UserDrivenResponsesBuilder, UserDrivenResponses

def test_builder_builds_userdrivenresponses():
    Builder = UserDrivenResponsesBuilder()

    actual = Builder.build()
    assert isinstance(actual,UserDrivenResponses)

