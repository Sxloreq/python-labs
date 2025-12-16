from users import Administrator, RegularUser, GuestUser
from access_control import AccessControl

def main():
    system = AccessControl()

    admin = Administrator("admin", "admin123", permissions=["manage_users"])
    user = RegularUser("ivan", "qwerty")
    guest = GuestUser("guest_user")

    system.add_user(admin)
    system.add_user(user)
    system.add_user(guest)

    print("--- Система авторизації ---")
    login = input("Введіть логін: ")
    pwd = input("Введіть пароль: ")

    current_user = system.authenticate_user(login, pwd)

    if current_user:
      
        role = type(current_user).__name__
        print(f"\n[УСПІХ] Вітаємо, {current_user.username}!")
        print(f"Ваша роль у системі: {role}")

        if role == "Administrator":
            print(f"Ваші права: {current_user.permissions}")
    else:
        print("\n[ПОМИЛКА] Доступ заборонено: невірні дані.")

if __name__ == "__main__":
    main()
