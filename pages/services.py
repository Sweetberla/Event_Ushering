from nicegui import ui
from .navigation import create_navigation

def services():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section
        with ui.card().classes('w-full p-8 text-center bg-gradient-to-r from-blue-50 to-green-50'):
            ui.label('Our Ushering Services').classes('text-3xl font-bold text-gray-800 mb-4')
            ui.label('Comprehensive Event Support Tailored to Your Needs').classes('text-lg text-gray-600')
        
        # Main services
        with ui.row().classes('w-full gap-6 mt-8'):
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('favorite', size='3rem').classes('text-pink-600 mb-4')
                ui.label('Wedding Ushering').classes('text-xl font-bold mb-3')
                ui.markdown('''
                **Complete Wedding Support:**
                - Guest seating coordination
                - Ceremony processional guidance
                - Reception assistance
                - Gift table management
                - Special needs accommodation
                ''').classes('text-gray-600')
            
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('business_center', size='3rem').classes('text-blue-600 mb-4')
                ui.label('Corporate Events').classes('text-xl font-bold mb-3')
                ui.markdown('''
                **Professional Business Support:**
                - Registration and check-in
                - VIP guest assistance
                - Meeting room coordination
                - Networking facilitation
                - Protocol management
                ''').classes('text-gray-600')
        
        # Additional services
        with ui.row().classes('w-full gap-6 mt-6'):
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('celebration', size='3rem').classes('text-purple-600 mb-4')
                ui.label('Private Celebrations').classes('text-xl font-bold mb-3')
                ui.markdown('''
                **Party & Event Management:**
                - Guest welcome and guidance
                - Entertainment coordination
                - Dining service support
                - Activity facilitation
                - Crowd management
                ''').classes('text-gray-600')
            
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('church', size='3rem').classes('text-green-600 mb-4')
                ui.label('Religious Ceremonies').classes('text-xl font-bold mb-3')
                ui.markdown('''
                **Respectful Ceremony Support:**
                - Congregation guidance
                - Special service coordination
                - Cultural sensitivity
                - Accessibility assistance
                - Ceremonial protocol
                ''').classes('text-gray-600')
        
        # Brand activations service
        with ui.row().classes('w-full gap-6 mt-6'):
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('rocket_launch', size='3rem').classes('text-orange-600 mb-4')
                ui.label('Brand Activations').classes('text-xl font-bold mb-3')
                ui.markdown('''
                **Dynamic Brand Experience Management:**
                - Product launch coordination
                - Brand ambassador management
                - Interactive experience facilitation
                - Guest engagement and interaction
                - Brand representation and promotion
                - Event flow and crowd control
                - VIP and media coordination
                - Brand activation setup and breakdown
                ''').classes('text-gray-600')
        
        
        # Service packages
        with ui.card().classes('w-full p-8 mt-8'):
            ui.label('Service Packages').classes('text-2xl font-bold text-center mb-6')
            
            with ui.row().classes('w-full gap-6'):
                # Basic package
                with ui.card().classes('flex-1 p-6 border-2 border-blue-200'):
                    ui.label('Essential Package').classes('text-xl font-bold text-blue-600 mb-3')
                    ui.label('Perfect for smaller events').classes('text-gray-600 mb-4')
                    ui.markdown('''
                    **Includes:**
                    - 4-6 professional ushers
                    - 4 hours of service
                    - Basic guest seating assistance
                    - Event day coordination
                    - Professional uniforms
                    
                    **Starting at $200**
                    ''').classes('text-sm')
                    ui.button('Contact for Pricing', on_click=lambda: ui.navigate.to('/contact')).classes('w-full mt-4 bg-blue-600 hover:bg-blue-700 text-white')
                
                # Premium package
                with ui.card().classes('flex-1 p-6 border-2 border-purple-200 bg-purple-50'):
                    ui.label('Premium Package').classes('text-xl font-bold text-purple-600 mb-3')
                    ui.label('Most popular choice').classes('text-gray-600 mb-4')
                    ui.markdown('''
                    **Includes:**
                    - 6-10 professional ushers
                    - 6-hour service duration
                    - Complete guest management
                    - Pre-event consultation
                    - Coordination with vendors
                                
                      **Starting at $500**          
                    ''').classes('text-sm')
                    ui.button('Contact for Pricing', on_click=lambda: ui.navigate.to('/contact')).classes('w-full mt-4 bg-purple-600 hover:bg-purple-700 text-white')
                
                # Luxury package
                with ui.card().classes('flex-1 p-6 border-2 border-gold-200'):
                    ui.label('Luxury Package').classes('text-xl font-bold text-yellow-600 mb-3')
                    ui.label('Full-service experience').classes('text-gray-600 mb-4')
                    ui.markdown('''
                    **Includes:**
                    - 10-20 professional ushers
                    - Full-day service
                    - Event coordination
                    - Setup assistance
                    - VIP guest services
                    - Post-event cleanup
                                
                      **Starting at $1000**
                    ''').classes('text-sm')
                    ui.button('Contact for Pricing', on_click=lambda: ui.navigate.to('/contact')).classes('w-full mt-4 bg-yellow-600 hover:bg-yellow-700 text-white')
        
        # Additional services
        with ui.card().classes('w-full p-8 mt-8 bg-gray-50'):
            ui.label('Additional Services Available').classes('text-2xl font-bold mb-4')
            with ui.row().classes('w-full gap-8'):
                with ui.column().classes('flex-1'):
                    ui.label('Event Coordination').classes('font-bold mb-2')
                    ui.label('Timeline management and vendor coordination')
                    
                with ui.column().classes('flex-1'):
                    ui.label('Special Needs Support').classes('font-bold mb-2')
                    ui.label('Accessibility assistance and accommodation')
                
                with ui.column().classes('flex-1'):
                    ui.label('Multilingual Staff').classes('font-bold mb-2')
                    ui.label('Ushers fluent in multiple languages')