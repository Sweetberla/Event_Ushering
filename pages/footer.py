from nicegui import ui
from .navigation import create_navigation

def footer():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section
        with ui.card().classes('w-full p-8 text-center bg-white'):
            ui.label('Company Information').classes('text-3xl font-bold text-black mb-4')
            ui.label('Everything You Need to Know About Our Business').classes('text-lg text-black mb-6')
        
        # Main footer content
        with ui.row().classes('w-full gap-8 mt-8'):
            # Company info
            with ui.card().classes('flex-1 p-8 bg-white'):
                ui.label('Bellyns Ushering Hub').classes('text-2xl font-bold text-black mb-4')
                ui.label('Professional ushering services for memorable events').classes('text-black mb-6')
                
                ui.label('Social Media').classes('text-lg font-bold text-black mb-4')
                with ui.column().classes('gap-3'):
                    with ui.row().classes('items-center gap-3'):
                        ui.icon('facebook').classes('text-2xl text-black mb-2')
                        ui.label('Facebook: bellyns ushering hub').classes('text-black mb-2')
                    with ui.row().classes('items-center gap-3'):
                        ui.icon('camera_alt').classes('text-2xl text-black mb-2')
                        ui.label('Instagram: @bellyns_usheringhub').classes('text-black mb-2')
                    with ui.row().classes('items-center gap-3'):
                        ui.icon('music_note').classes('text-2xl text-black mb-2')
                        ui.label('TikTok: @bellyns_usheringhub').classes('text-black mb-2')
            
            # Quick links
            with ui.card().classes('flex-1 p-8 bg-white mb-6'):
                ui.label('Quick Links').classes('text-lg font-bold text-black mb-4')
                ui.link('Home', '/').classes('text-black hover:text-black mb-3 text-lg')
                ui.link('About Us', '/about').classes('text-black hover:text-black mb-3 text-lg')
                ui.link('Our Services', '/services').classes('text-black hover:text-black mb-3 text-lg')
                ui.link('Gallery', '/gallery').classes('text-black hover:text-black mb-3 text-lg')
                ui.link('Testimonials', '/testimonials').classes('text-black hover:text-black mb-3 text-lg')
                ui.link('Contact', '/contact').classes('text-black hover:text-black mb-3 text-lg')
                ui.link('FAQs', '/faqs').classes('text-black hover:text-black mb-3 text-lg')
        
        # Services and Contact
        with ui.row().classes('w-full gap-8 mt-6'):
            # Services
            with ui.card().classes('flex-1 p-8 bg-white mb-6'):
                ui.label('Our Services').classes('text-lg font-bold text-black mb-4')
                ui.label('Wedding Ushering').classes('text-black mb-2')
                ui.label('Corporate Events').classes('text-black' \
                ' mb-2')
                ui.label('Private Parties').classes('text-black block mb-2')
                ui.label('Religious Ceremonies').classes('text-black block mb-2')
                ui.label('Special Events').classes('text-black block mb-2')
            
            # Contact info
            with ui.card().classes('flex-1 p-8 bg-white mb-6'):
                ui.label('Contact Information').classes('text-lg font-bold text-black mb-4')
                with ui.row().classes('items-center gap-3 mb-3'):
                    ui.icon('phone').classes('text-black-400 text-xl')
                    ui.label('+233596273835').classes('text-black-300')
                with ui.row().classes('items-center gap-3 mb-3'):
                    ui.icon('email').classes('text-black-400 text-xl')
                    ui.label('bellynsushering878@gmail.com').classes('text-black-300')
                with ui.row().classes('items-center gap-3 mb-3'):
                    ui.icon('location_on').classes('text-black-400 text-xl')
                    with ui.column():
                        ui.label('Ashaley Botwe').classes('text-black-300')
                with ui.row().classes('items-center gap-3 mb-3'):
                    ui.icon('schedule').classes('text-black-400 text-xl')
                    with ui.column():
                        ui.label('Mon-Fri: 9:00 AM - 6:00 PM').classes('text-black-300')
                        ui.label('Sat-Sun: 10:00 AM - 4:00 PM').classes('text-black-300')
        
        # Legal and policies
        with ui.card().classes('w-full p-8 mt-8 bg-black'):
            ui.label('Legal Information').classes('text-xl font-bold text-yellow-600 mb-4')
            with ui.row().classes('w-full justify-between items-center'):
                ui.label('© 2025 Bellyns Ushering Hub. All rights reserved.').classes('text-yellow-600')
                with ui.row().classes('gap-6'):
                    ui.link('Privacy Policy', '#').classes('text-yellow-600 hover:text-black mb-4')
                    ui.link('Terms of Service', '#').classes('text-yellow-600 hover:text-black mb-4')
                    ui.link('Cookie Policy', '#').classes('text-yellow-600 hover:text-black mb-4')
