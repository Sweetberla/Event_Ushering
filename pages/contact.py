from nicegui import ui
from .navigation import create_navigation
import json
from datetime import datetime
import os

def contact():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section with background image
        with ui.card().classes('w-full p-6 md:p-8 text-center relative overflow-hidden').style('background-image: url("/assets/ushers3.jpg.JPEG"); background-size: cover; background-position: center;'):
            # Light overlay for better text readability
            ui.element('div').classes('absolute inset-0 bg-black opacity-30')
            # Content on top of overlay
            with ui.column().classes('relative z-10'):
                ui.label('Contact & Booking').classes('text-2xl md:text-3xl lg:text-4xl font-bold text-white mb-4 drop-shadow-lg')
                ui.label('Get in Touch to Plan Your Perfect Event').classes('text-base md:text-lg text-white drop-shadow-lg')
        
        with ui.row().classes('w-full gap-4 md:gap-8 mt-8 flex-col lg:flex-row'):
            # Contact form
            with ui.card().classes('flex-1 p-4 md:p-8 bg-white'):
                ui.label('Request a Quote').classes('text-xl md:text-2xl font-bold text-black mb-6')
                
                with ui.column().classes('w-full gap-3 md:gap-4'):
                    name_input = ui.input('Full Name').classes('w-full').props('outlined')
                    email_input = ui.input('Email Address').classes('w-full').props('outlined type=email')
                    phone_input = ui.input('Phone Number').classes('w-full').props('outlined type=tel')
                    
                    event_type = ui.select(['Wedding', 'Corporate Event', 'Private Party', 'Religious Ceremony', 'Other'], 
                                         label='Event Type').classes('w-full').props('outlined')
                    
                    with ui.row().classes('w-full gap-3 md:gap-4 flex-col sm:flex-row'):
                        event_date = ui.input('Event Date').classes('flex-1').props('outlined type=date')
                        guest_count = ui.input('Expected Guests').classes('flex-1').props('outlined type=number')
                    
                    venue_input = ui.input('Venue/Location').classes('w-full').props('outlined')
                    
                    message_input = ui.textarea('Additional Details').classes('w-full').props('outlined rows=4')
                    
                    def submit_form():
                        if name_input.value and email_input.value and phone_input.value:
                            # Create quote request data
                            quote_data = {
                                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                'name': name_input.value,
                                'email': email_input.value,
                                'phone': phone_input.value,
                                'event_type': event_type.value if event_type.value else 'Not specified',
                                'event_date': event_date.value if event_date.value else 'Not specified',
                                'guest_count': guest_count.value if guest_count.value else 'Not specified',
                                'venue': venue_input.value if venue_input.value else 'Not specified',
                                'message': message_input.value if message_input.value else 'No additional details'
                            }
                            
                            # Save to JSON file
                            quotes_file = 'quote_requests.json'
                            try:
                                # Read existing quotes
                                if os.path.exists(quotes_file):
                                    with open(quotes_file, 'r') as f:
                                        quotes = json.load(f)
                                else:
                                    quotes = []
                                
                                # Add new quote
                                quotes.append(quote_data)
                                
                                # Save back to file
                                with open(quotes_file, 'w') as f:
                                    json.dump(quotes, f, indent=4)
                                
                                ui.notify('Thank you! Your quote request has been saved. We will contact you within 24 hours.', type='positive')
                                
                                # Clear form
                                name_input.value = ''
                                email_input.value = ''
                                phone_input.value = ''
                                event_type.value = None
                                event_date.value = ''
                                guest_count.value = ''
                                venue_input.value = ''
                                message_input.value = ''
                            except Exception as e:
                                ui.notify(f'Error saving quote request. Please try again or call us directly.', type='negative')
                                print(f'Error: {e}')
                        else:
                            ui.notify('Please fill in all required fields (Name, Email, Phone)', type='warning')
                    
                    ui.button('Submit Request', on_click=submit_form).classes('w-full bg-black hover:bg-gray-800 text-white py-2.5 md:py-3 rounded-lg font-semibold mt-4 transition-all')
            
            # Contact information
            with ui.card().classes('flex-1 p-4 md:p-8 bg-white'):
                ui.label('Get In Touch').classes('text-xl md:text-2xl font-bold text-black mb-6')
                
                with ui.column().classes('gap-4 md:gap-6'):
                    with ui.row().classes('items-center gap-3 mb-3 md:mb-4'):
                        ui.icon('phone').classes('text-black text-xl md:text-2xl')
                        with ui.column():
                            ui.label('Phone').classes('font-semibold text-black text-sm md:text-base')
                            ui.label('+233596273835').classes('text-black text-sm md:text-base')
                    
                    with ui.row().classes('items-center gap-3 mb-3 md:mb-4'):
                        ui.icon('email').classes('text-black text-xl md:text-2xl')
                        with ui.column():
                            ui.label('Email').classes('font-semibold text-black text-sm md:text-base')
                            ui.label('bellynsushering878@gmail.com').classes('text-black text-sm md:text-base break-all')
                    
                    with ui.row().classes('items-center gap-3 mb-3 md:mb-4'):
                        ui.icon('location_on').classes('text-black text-xl md:text-2xl')
                        with ui.column():
                            ui.label('Location').classes('font-semibold text-black text-sm md:text-base')
                            ui.label('Ashaley Botwe').classes('text-black text-sm md:text-base')
                    
                    with ui.row().classes('items-center gap-3 md:gap-4'):
                        ui.icon('schedule', size='1.5rem').classes('text-black md:text-2xl')
                        with ui.column():
                            ui.label('Business Hours').classes('font-bold text-black text-sm md:text-base')
                            ui.label('Mon-Fri: 9:00 AM - 6:00 PM').classes('text-black text-sm md:text-base')
                            ui.label('Sat-Sun: 10:00 AM - 4:00 PM').classes('text-black text-sm md:text-base')
        
        # Service areas with background image
        with ui.card().classes('w-full p-4 md:p-8 mt-8 relative overflow-hidden').style('background-image: url("/assets/brandact.jpg"); background-size: cover; background-position: center;'):
            # Light overlay
            ui.element('div').classes('absolute inset-0 bg-white opacity-20')
            # Content on top
            with ui.column().classes('relative z-10'):
                ui.label('Service Areas').classes('text-xl md:text-2xl font-bold text-center text-black mb-4 md:mb-6')
                ui.label('We proudly serve the following metropolitan areas:').classes('text-center text-black text-sm md:text-base mb-4 md:mb-6')
                
                with ui.row().classes('w-full gap-4 md:gap-6 justify-center flex-wrap'):
                    with ui.column().classes('text-center min-w-[120px]'):
                        ui.icon('location_city', size='2rem').classes('text-black mb-2')
                        ui.label('Downtown Metro').classes('font-bold text-black text-sm md:text-base')
                        ui.label('Full service area').classes('text-black text-xs md:text-sm')
                    
                    with ui.column().classes('text-center min-w-[120px]'):
                        ui.icon('home', size='2rem').classes('text-black mb-2')
                        ui.label('Suburban Areas').classes('font-bold text-black text-sm md:text-base')
                        ui.label('Within 50 miles').classes('text-black text-xs md:text-sm')
                    
                    with ui.column().classes('text-center min-w-[120px]'):
                        ui.icon('nature', size='2rem').classes('text-black mb-2')
                        ui.label('Resort Venues').classes('font-bold text-black text-sm md:text-base')
                        ui.label('Special arrangements').classes('text-black text-xs md:text-sm')
        
        # FAQ quick links
        with ui.card().classes('w-full p-4 md:p-8 mt-8 bg-white'):
            ui.label('Quick Information').classes('text-xl md:text-2xl font-bold text-black mb-4 md:mb-6')
            
            with ui.row().classes('w-full gap-4 md:gap-6 flex-col lg:flex-row'):
                with ui.card().classes('flex-1 p-4 md:p-6 bg-white hover:shadow-lg transition-shadow border border-gray-200'):
                    ui.icon('help', size='2rem').classes('text-black mb-3')
                    ui.label('Frequently Asked Questions').classes('font-bold text-black mb-2 text-sm md:text-base')
                    ui.label('Find answers to common questions about our services').classes('text-black text-xs md:text-sm')
                    ui.button('View FAQs', on_click=lambda: ui.navigate.to('/faqs')).classes('mt-3 bg-black hover:bg-gray-800 text-white px-4 py-2 rounded transition-all text-sm md:text-base')
                
                with ui.card().classes('flex-1 p-4 md:p-6 bg-white hover:shadow-lg transition-shadow border border-gray-200'):
                    ui.icon('info', size='2rem').classes('text-black mb-3')
                    ui.label('Service Packages').classes('font-bold text-black mb-2 text-sm md:text-base')
                    ui.label('Learn about our different service options and pricing').classes('text-black text-xs md:text-sm')
                    ui.button('View Services', on_click=lambda: ui.navigate.to('/services')).classes('mt-3 bg-black hover:bg-gray-800 text-white px-4 py-2 rounded transition-all text-sm md:text-base')
                
                with ui.card().classes('flex-1 p-4 md:p-6 bg-white hover:shadow-lg transition-shadow border border-gray-200'):
                    ui.icon('photo_library', size='2rem').classes('text-black mb-3')
                    ui.label('Our Work').classes('font-bold text-black mb-2 text-sm md:text-base')
                    ui.label('See examples of our professional ushering services').classes('text-black text-xs md:text-sm')
                    ui.button('View Gallery', on_click=lambda: ui.navigate.to('/gallery')).classes('mt-3 bg-black hover:bg-gray-800 text-white px-4 py-2 rounded transition-all text-sm md:text-base')
        
        # Emergency contact
        with ui.card().classes('w-full p-4 md:p-6 mt-8 bg-black border-l-4 border-black'):
            with ui.row().classes('items-center gap-3 md:gap-4 flex-col sm:flex-row text-center sm:text-left'):
                ui.icon('emergency', size='2rem').classes('text-yellow-600')
                with ui.column():
                    ui.label('Emergency/Last-Minute Bookings').classes('font-bold text-yellow-600 text-sm md:text-base')
                    ui.label('For urgent requests within 48 hours, call our emergency line: +233596273835').classes('text-yellow-600 text-xs md:text-sm')