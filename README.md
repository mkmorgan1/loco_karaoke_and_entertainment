# Loco Karaoke & Entertainment

A Django web application for managing karaoke and entertainment events. Built with a country-themed design and comprehensive event management system.

## 🎤 Features

- **Event Management**: Create and manage karaoke nights, live music, comedy shows, and special events
- **Admin Interface**: Full Django admin integration for easy event management
- **Home Page**: Welcome page with upcoming events calendar
- **Country Theme**: Beautiful country-inspired color palette and design
- **Responsive Design**: Mobile-friendly Bootstrap-based interface
- **User Access Control**: Admin-only access to event management features

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Python**: 3.12.3 (managed with pyenv)
- **Package Management**: pip
- **Version Control**: Git

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- **Python 3.12.3** (recommended to use pyenv)
- **MySQL Server**
- **Git**

### Installing pyenv (macOS)

```bash
# Install pyenv using Homebrew
brew install pyenv

# Add to your shell profile (~/.bash_profile, ~/.zshrc, etc.)
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Restart your shell or source the profile
source ~/.bash_profile
```

### Installing MySQL

```bash
# Install MySQL using Homebrew
brew install mysql

# Start MySQL service
brew services start mysql
```

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone git@github.com:mkmorgan1/loco_karaoke_and_entertainment.git
   cd loco_karaoke_and_entertainment
   ```

2. **Set up Python environment**
   ```bash
   # Install Python 3.12.3 using pyenv
   pyenv install 3.12.3
   pyenv local 3.12.3
   
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   # Create MySQL database
   mysql -u root -p
   CREATE DATABASE loco_karaoke CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   EXIT;
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
loco_karaoke_and_entertainment/
├── karaoke/                    # Main Django app
│   ├── migrations/            # Database migrations
│   ├── static/               # Static files (CSS, JS, images)
│   ├── templates/            # HTML templates
│   ├── admin.py              # Admin interface configuration
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing
│   └── views.py              # View functions
├── loco_karaoke/             # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── static/                   # Global static files
│   └── logo.png              # Logo image
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎯 Key Features Explained

### Event Management
- **Event Types**: Karaoke Night, Live Music, Comedy Night, Dance Party, Special Event
- **Event Details**: Title, description, date, time, location, capacity, featured status
- **Admin Interface**: Full CRUD operations through Django admin

### Access Control
- **Public Access**: Anyone can view the home page and upcoming events
- **Admin Access**: Only superusers can access the admin interface and add/edit events
- **Conditional UI**: "Add Event" buttons and admin links only appear for superusers

### Design System
- **Country Theme**: Warm browns, golds, and cream colors
- **Responsive**: Mobile-first Bootstrap design
- **Custom Logo**: Integrated logo with proper sizing and styling

## 🔧 Configuration

### Database Settings
The project is configured to use MySQL with the following default settings:
- Database: `loco_karaoke`
- User: `root`
- Password: (empty)
- Host: `localhost`
- Port: `3306`

### Static Files
Static files are configured to be served from:
- Development: `static/` directory
- Production: `staticfiles/` (after running `collectstatic`)

## 🚀 Deployment

For production deployment:

1. **Set up environment variables**
   ```bash
   export DJANGO_SETTINGS_MODULE=loco_karaoke.settings
   export SECRET_KEY='your-secret-key-here'
   export DEBUG=False
   ```

2. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Configure your web server** (nginx, Apache, etc.)

4. **Set up a production database** with proper credentials

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Matt Morgan**
- GitHub: [@mkmorgan1](https://github.com/mkmorgan1)

## 🙏 Acknowledgments

- Django community for the excellent web framework
- Bootstrap team for the responsive CSS framework
- Font Awesome for the beautiful icons

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/mkmorgan1/loco_karaoke_and_entertainment/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer directly

---

**Happy Karaoke! 🎤🎵** 