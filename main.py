from nicegui import ui, app
import os
from pages import home, about, services, gallery, testimonials, contact, faqs, footer

# Serve static files from assets folder
app.add_static_files('/assets', 'assets')

# Register page routes using the imported functions
ui.page('/')(home.home)
ui.page('/about')(about.about)
ui.page('/services')(services.services)
ui.page('/gallery')(gallery.gallery)
ui.page('/testimonials')(testimonials.testimonials)
ui.page('/contact')(contact.contact)
ui.page('/faqs')(faqs.faqs)
ui.page('/footer')(footer.footer)

ui.run(host="0.0.0.0",port=int(os.getenv("PORT",8080)))