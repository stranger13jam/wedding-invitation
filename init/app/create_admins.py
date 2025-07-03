import os
import psycopg2


ROLE_ADMIN = "admin"

db_config = {
      "host": "localhost", # for local development
      # "host": os.getenv("POSTGRES_HOST"), # for production
      "port": os.getenv("POSTGRES_PORT"),
      "dbname": os.getenv("POSTGRES_DB"),
      "user": os.getenv("POSTGRES_USER"),
      "password": os.getenv("POSTGRES_PASSWORD"),
}

users_to_insert = {
      "first_name": os.getenv("ADMIN_FIRST_NAME").split(","),
      "last_name": os.getenv("ADMIN_LAST_NAME").split(","),
      "middle_name": os.getenv("ADMIN_MIDDLE_NAME").split(","),
      "short_name": os.getenv("ADMIN_SHORT_NAME").split(","),
      "phone": os.getenv("ADMIN_PHONE").split(","),
      "telegram": os.getenv("ADMIN_TELEGRAM").split(",")
}


def create_admins():
      try:
            with psycopg2.connect(**db_config) as conn:
                  with conn.cursor() as cur:
                        for i in range(len(users_to_insert["first_name"])):
                              cur.execute(
                                    """
                                    INSERT INTO public.users (first_name, middle_name, last_name, short_name, phone, telegram, role)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                                    """,
                                    (
                                          users_to_insert["first_name"][i],
                                          users_to_insert["middle_name"][i],
                                          users_to_insert["last_name"][i],
                                          users_to_insert["short_name"][i],
                                          users_to_insert["phone"][i],
                                          users_to_insert["telegram"][i],
                                          ROLE_ADMIN,
                                    )
                              )

                        conn.commit()
                        print(f"✅ Users added: {i+1}")
      except Exception as e:
            print(f"❌ Error when inserting users: {e}")


if __name__ == "__main__":
      create_admins()