from User_Responses import UserDrivenResponsesBuilder
from recommendations import get_recommendations


def main():
    builder = UserDrivenResponsesBuilder()
    built_responses = builder.add_genre_from_user() \
        .add_does_user_want_fiction() \
        .add_does_user_want_recently_published() \
        .add_does_user_want_staff_recommendations() \
        .add_does_user_know_the_book_title() \
        .build()

    recommendations = get_recommendations(built_responses)

    print(recommendations)



if __name__ == "__main__":
    main()