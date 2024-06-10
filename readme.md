
# QR Code Scanner with Django and Tailwind CSS

This is a web-based QR code scanner application built with Django for the backend and Tailwind CSS for the frontend. It uses the `html5-qrcode` library to scan and decode QR codes in real-time using the device's camera. The scanned content is displayed in a glassmorphic card with an animated rainbow background.

## Features

- Real-time QR code scanning using the device's camera
- Responsive design with Tailwind CSS
- Animated rainbow background
- Glassmorphic card to display QR code content

## Prerequisites

- Python 3.x
- Django 3.x or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Levi-Chinecherm/qr-code-scanner.git
   cd qr-code-scanner
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install django
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

## Running the Server

1. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:8000/scan/
   ```

## Customizing the Styling

The styling uses Tailwind CSS and custom CSS for specific animations and glassmorphic effects. You can find the custom styles in the `<style>` section of the `scanner.html` file:

```html
<style>
    body {
        background: linear-gradient(270deg, #ff6ec4, #7873f5);
        background-size: 400% 400%;
        animation: rainbow 10s ease infinite;
    }

    @keyframes rainbow {
        0%, 100% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
    }

    .glass {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
</style>
```

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
