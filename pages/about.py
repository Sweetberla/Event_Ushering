from nicegui import ui
from .navigation import create_navigation

def about():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section
        with ui.card().classes('w-full p-8 text-center bg-gradient-to-r from-purple-50 to-blue-50'):
            ui.label('About Our Events Ushering Service').classes('text-3xl font-bold text-gray-800 mb-4')
            ui.label('Professional, Reliable, and Dedicated to Excellence').classes('text-lg text-gray-600')
        
        # Mission section
        with ui.card().classes('w-full p-8 mt-8'):
            ui.label('Our Mission').classes('text-2xl font-bold text-purple-600 mb-4')
            ui.markdown('''
            To provide exceptional ushering services that enhance every event experience. We believe that professional, 
            courteous, and attentive service creates lasting impressions and contributes to the success of your special occasions.
            ''').classes('text-lg text-gray-700 leading-relaxed')
        
        # Team section
        with ui.row().classes('w-full gap-8 mt-8'):
            with ui.card().classes('flex-1 p-6'):
                ui.icon('groups', size='3rem').classes('text-blue-600 mb-4')
                ui.label('Experienced Team').classes('text-xl font-bold mb-3')
                ui.label('Our ushers are carefully selected and trained professionals with years of experience in hospitality and event management.').classes('text-gray-600')
            
            with ui.card().classes('flex-1 p-6'):
                ui.icon('star', size='3rem').classes('text-yellow-500 mb-4')
                ui.label('Quality Service').classes('text-xl font-bold mb-3')
                ui.label('We maintain the highest standards of professionalism, ensuring your guests receive warm, courteous, and efficient service.').classes('text-gray-600')
        
        # Values section
        with ui.card().classes('w-full p-8 mt-8'):
            ui.label('Our Core Values').classes('text-2xl font-bold text-center mb-6')
            with ui.row().classes('w-full gap-6'):
                with ui.column().classes('flex-1 text-center'):
                    ui.icon('handshake', size='2.5rem').classes('text-green-600 mb-3')
                    ui.label('Professionalism').classes('font-bold text-lg mb-2')
                    ui.label('Maintaining the highest standards in appearance, conduct, and service delivery')
                
                with ui.column().classes('flex-1 text-center'):
                    ui.icon('schedule', size='2.5rem').classes('text-blue-600 mb-3')
                    ui.label('Reliability').classes('font-bold text-lg mb-2')
                    ui.label('Punctual, dependable service you can count on for your important events')
                
                with ui.column().classes('flex-1 text-center'):
                    ui.icon('favorite', size='2.5rem').classes('text-red-600 mb-3')
                    ui.label('Hospitality').classes('font-bold text-lg mb-2')
                    ui.label('Warm, welcoming service that makes every guest feel valued and comfortable')
        
        # Experience section
        with ui.card().classes('w-full p-8 mt-8 bg-gray-50'):
            ui.label('Our Experience').classes('text-2xl font-bold mb-4')
            ui.markdown('''
            **Years of Excellence:** We have successfully provided ushering services for fifteen events, 
            from intimate gatherings to large-scale celebrations.
            
            **Event Types We Serve:**
            - Weddings and receptions
            - Corporate conferences and meetings
            - Gala dinners and award ceremonies
            - Private parties and celebrations
            - Religious ceremonies and cultural events
            - Product launches and exhibitions
            
            **What Sets Us Apart:**
            - Personalized service planning for each event
            - Professional uniforms and presentation
            - Flexible scheduling and last-minute accommodations
            - Comprehensive event coordination support
            ''').classes('text-gray-700 leading-relaxed')