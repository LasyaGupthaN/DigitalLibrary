from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User, RoleEnum
from app.auth import hash_password

def create_default_admin():
    db: Session = SessionLocal()

    admin_exists = db.query(User).filter(User.role == RoleEnum.admin).first()
    if admin_exists:
        print("✅ Admin already exists")
        db.close()
        return

    admin = User(
        name="Default Admin",
        email="admin@library.com",
        password=hash_password("admin123"),
        role=RoleEnum.admin
    )

    db.add(admin)
    db.commit()
    db.close()

    print("🚀 DEFAULT ADMIN CREATED:")
    print("    Email: admin@library.com")
    print("    Password: admin123")
