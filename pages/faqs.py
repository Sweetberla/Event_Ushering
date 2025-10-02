from nicegui import ui
from .navigation import create_navigation
import json
from datetime import datetime
import os

def faqs():
    create_navigation()
    
    def submit_inquiry(category, name_input, email_input, question_input):
        """Save FAQ inquiry to file"""
        if name_input.value and email_input.value and question_input.value:
            inquiry_data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'category': category,
                'name': name_input.value,
                'email': email_input.value,
                'question': question_input.value
            }
            
            inquiries_file = 'faq_inquiries.json'
            try:
                if os.path.exists(inquiries_file):
                    with open(inquiries_file, 'r') as f:
                        inquiries = json.load(f)
                else:
                    inquiries = []
                
                inquiries.append(inquiry_data)
                
                with open(inquiries_file, 'w') as f:
                    json.dump(inquiries, f, indent=4)
                
                ui.notify('Thank you! Your question has been submitted. We will respond via email.', type='positive')
                
                # Clear form
                name_input.value = ''
                email_input.value = ''
                question_input.value = ''
            except Exception as e:
                ui.notify('Error submitting question. Please try again or contact us directly.', type='negative')
                print(f'Error: {e}')
        else:
            ui.notify('Please fill in all fields', type='warning')
    
    def scroll_to_section(section):
        """Scroll to the specified FAQ section"""
        ui.notify(f'Scrolling to {section.title()} section', type='info')
        # JavaScript to smooth scroll to section using ID
        ui.run_javascript(f'''
            const target = document.getElementById('{section}');
            if (target) {{
                target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                // Add small offset for better visibility
                setTimeout(() => {{ window.scrollBy(0, -20); }}, 100);
            }}
        ''')
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section
        with ui.card().classes('w-full p-8 text-center bg-white from-orange-50 to-red-50'):
            ui.label('Frequently Asked Questions').classes('text-3xl md:text-4xl font-bold text-gray-800 mb-4')
            ui.label('Find Answers to Common Questions About Our Services').classes('text-base md:text-lg text-gray-600')
        
        # FAQ categories - responsive grid layout
        with ui.row().classes('w-full gap-3 mt-8 justify-center flex-wrap'):
            ui.button('General', on_click=lambda: scroll_to_section('general')).classes('bg-black hover:bg-blue-700 text-white px-6 py-2.5 rounded-lg font-medium shadow-md transition-all w-full sm:w-auto min-w-[120px]')
            ui.button('Booking', on_click=lambda: scroll_to_section('booking')).classes('bg-black hover:bg-green-700 text-white px-6 py-2.5 rounded-lg font-medium shadow-md transition-all w-full sm:w-auto min-w-[120px]')
            ui.button('Pricing', on_click=lambda: scroll_to_section('pricing')).classes('bg-black hover:bg-purple-700 text-white px-6 py-2.5 rounded-lg font-medium shadow-md transition-all w-full sm:w-auto min-w-[120px]')
            ui.button('Services', on_click=lambda: scroll_to_section('services')).classes('bg-black hover:bg-orange-700 text-white px-6 py-2.5 rounded-lg font-medium shadow-md transition-all w-full sm:w-auto min-w-[120px]')
        
        # General FAQs
        general_section = ui.card().classes('w-full p-4 md:p-8 mt-8').props('id="general-section"')
        with general_section:
            ui.label('General Questions').classes('text-xl md:text-2xl font-bold text-black mb-6').props('id="general"')
            
            with ui.expansion('What is professional ushering?', icon='help').classes('w-full mb-4'):
                ui.markdown('''
                Professional ushering involves trained staff who assist with guest management, seating coordination, 
                and general hospitality at events. Our ushers help ensure smooth event flow, assist guests with 
                directions, manage crowd control, and provide a welcoming presence that enhances the overall event experience.
                ''')
            
            with ui.expansion('How experienced is your team?', icon='groups').classes('w-full mb-4'):
                ui.markdown('''
                Our team consists of carefully selected professionals with extensive experience in hospitality and event management. 
                Each usher undergoes comprehensive training and has worked at numerous events ranging from intimate gatherings 
                to large-scale celebrations with 500+ guests. We maintain high standards through ongoing training and performance evaluation.
                ''')
            
            with ui.expansion('What areas do you serve?', icon='location_on').classes('w-full mb-4'):
                ui.markdown('''
                We primarily serve the metropolitan area and surrounding suburbs within a 50-mile radius. 
                For venues beyond this range, we can arrange special accommodations with additional travel fees. 
                We also provide services for destination events and resort venues with advance planning.
                ''')
            
            # General inquiry form
            with ui.expansion('Ask a General Question', icon='question_answer').classes('w-full mb-4 bg-gray-50'):
                with ui.column().classes('gap-3'):
                    gen_name = ui.input('Your Name').classes('w-full').props('outlined')
                    gen_email = ui.input('Your Email').classes('w-full').props('outlined type=email')
                    gen_question = ui.textarea('Your Question').classes('w-full').props('outlined rows=3')
                    ui.button('Submit Question', on_click=lambda: submit_inquiry('General', gen_name, gen_email, gen_question)).classes('bg-black hover:bg-gray-800 text-white px-4 py-2 rounded')
        
        # Booking FAQs
        booking_section = ui.card().classes('w-full p-4 md:p-8 mt-8').props('id="booking-section"')
        with booking_section:
            ui.label('Booking & Scheduling').classes('text-xl md:text-2xl font-bold text-black mb-6').props('id="booking"')
            
            with ui.expansion('How far in advance should I book?', icon='schedule').classes('w-full mb-4'):
                ui.markdown('''
                We recommend booking at least 4-6 weeks in advance for optimal availability, especially during peak 
                wedding season (May-October). However, we can accommodate last-minute requests when possible. 
                For urgent bookings within 48 hours, please call our emergency line at +233596273835.
                ''')
            
            with ui.expansion('Can I make changes to my booking?', icon='edit').classes('w-full mb-4'):
                ui.markdown('''
                Yes, we understand that event details can change. Modifications can be made up to 72 hours before 
                your event without additional fees. Changes within 72 hours may incur adjustment fees depending 
                on the nature of the modification. We always work with you to accommodate necessary changes.
                ''')
            
            with ui.expansion('What is your cancellation policy?', icon='cancel').classes('w-full mb-4'):
                ui.markdown('''
                - **More than 2 weeks notice**: Full refund minus 10% processing fee
                - **1-2 weeks notice**: 50% refund
                - **Less than 1 week**: 25% refund
                - **Less than 48 hours**: No refund, but credit toward future booking
                
                We understand emergencies happen and will work with you on a case-by-case basis.
                ''')
            
            # Booking inquiry form
            with ui.expansion('Ask a Booking Question', icon='question_answer').classes('w-full mb-4 bg-gray-50'):
                with ui.column().classes('gap-3'):
                    book_name = ui.input('Your Name').classes('w-full').props('outlined')
                    book_email = ui.input('Your Email').classes('w-full').props('outlined type=email')
                    book_question = ui.textarea('Your Question').classes('w-full').props('outlined rows=3')
                    ui.button('Submit Question', on_click=lambda: submit_inquiry('Booking', book_name, book_email, book_question)).classes('bg-black hover:bg-gray-800 text-white px-4 py-2 rounded')
        
        # Pricing FAQs
        pricing_section = ui.card().classes('w-full p-4 md:p-8 mt-8').props('id="pricing-section"')
        with pricing_section:
            ui.label('Pricing & Packages').classes('text-xl md:text-2xl font-bold text-black mb-6').props('id="pricing"')
            
            with ui.expansion('How is pricing determined?', icon='attach_money').classes('w-full mb-4'):
                ui.markdown('''
                Pricing is based on several factors:
                - Number of ushers required
                - Duration of service
                - Event complexity and size
                - Location and travel requirements
                - Additional services requested
                
                We provide transparent, detailed quotes with no hidden fees.
                ''')
            
            with ui.expansion('Do you offer package deals?', icon='local_offer').classes('w-full mb-4'):
                ui.markdown('''
                Yes! We offer three main packages:
                - **Essential Package**: 4-6 ushers, 4 hours, basic coordination
                - **Premium Package**: 6-8 ushers, 6 hours, full guest management
                - **Luxury Package**: 6-10 ushers, full-day service, complete coordination
                
                Custom packages are also available for unique requirements.
                ''')
            
            with ui.expansion('Are there additional fees?', icon='receipt').classes('w-full mb-4'):
                ui.markdown('''
                Additional fees may apply for:
                - Travel beyond our standard service area
                - Events requiring special uniforms or attire
                - Overtime beyond contracted hours
                - Last-minute booking requests
                - Special equipment or setup requirements
                
                All potential additional fees are discussed upfront in your quote.
                ''')
            
            # Pricing inquiry form
            with ui.expansion('Ask a Pricing Question', icon='question_answer').classes('w-full mb-4 bg-gray-50'):
                with ui.column().classes('gap-3'):
                    price_name = ui.input('Your Name').classes('w-full').props('outlined')
                    price_email = ui.input('Your Email').classes('w-full').props('outlined type=email')
                    price_question = ui.textarea('Your Question').classes('w-full').props('outlined rows=3')
                    ui.button('Submit Question', on_click=lambda: submit_inquiry('Pricing', price_name, price_email, price_question)).classes('bg-black hover:bg-gray-800 text-white px-4 py-2 rounded')
        
        # Services FAQs
        services_section = ui.card().classes('w-full p-4 md:p-8 mt-8').props('id="services-section"')
        with services_section:
            ui.label('Services & Logistics').classes('text-xl md:text-2xl font-bold text-black mb-6').props('id="services"')
            
            with ui.expansion('What do your ushers wear?', icon='checkroom').classes('w-full mb-4'):
                ui.markdown('''
                Our ushers dress professionally in formal attire appropriate for your event:
                - **Weddings**: Black suits or dresses, can match your color scheme
                - **Corporate Events**: Business formal attire
                - **Special Events**: Attire coordinated with event theme
                
                We can also accommodate specific uniform requirements with advance notice.
                ''')
            
            with ui.expansion('Do you provide multilingual services?', icon='translate').classes('w-full mb-4'):
                ui.markdown('''
                Yes, we have team members fluent in multiple local languages including Twi, Ewe, and Hausa. 
                Please specify language requirements when booking so we can assign appropriate staff members 
                to your event. Additional languages may be available upon request.
                ''')
            
            with ui.expansion('Can you coordinate with other vendors?', icon='handshake').classes('w-full mb-4'):
                ui.markdown('''
                Absolutely! Our ushers are experienced in working with wedding planners, caterers, photographers, 
                and other event vendors. We can help coordinate timing, assist with vendor setup areas, 
                and ensure smooth communication throughout your event.
                ''')
            
            # Services inquiry form
            with ui.expansion('Ask a Services Question', icon='question_answer').classes('w-full mb-4 bg-gray-50'):
                with ui.column().classes('gap-3'):
                    serv_name = ui.input('Your Name').classes('w-full').props('outlined')
                    serv_email = ui.input('Your Email').classes('w-full').props('outlined type=email')
                    serv_question = ui.textarea('Your Question').classes('w-full').props('outlined rows=3')
                    ui.button('Submit Question', on_click=lambda: submit_inquiry('Services', serv_name, serv_email, serv_question)).classes('bg-black hover:bg-gray-800 text-white px-4 py-2 rounded')
        
        # Contact section
        with ui.card().classes('w-full p-6 md:p-8 mt-8 text-center bg-black text-black'):
            ui.label('Still Have Questions?').classes('text-xl md:text-2xl  text-yellow-600 font-bold mb-4')
            ui.label('We\'re here to help! Contact us for personalized assistance.').classes('text-base text-yellow-600 md:text-lg mb-6')
            with ui.row().classes('gap-2 md:gap-4 justify-center flex-wrap'):
                ui.button('Contact Us', on_click=lambda: ui.navigate.to('/contact')).classes('bg-yellow-600 text-black hover:bg-yellow-700 hover:text-black px-6 md:px-8 py-2 md:py-3 rounded-lg font-semibold text-sm md:text-base')
                ui.button('Request Quote', on_click=lambda: ui.navigate.to('/contact')).classes('bg-yellow-600 border-2 border-black text-black hover:bg-yellow-700 hover:text-black px-6 md:px-8 py-2 md:py-3 rounded-lg font-semibold text-sm md:text-base')