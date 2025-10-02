from nicegui import ui
from .navigation import create_navigation

def home():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Hero section
        with ui.card().classes('w-full p-8 bg-gradient-to-r from-black-50 to-black-50 border-0 shadow-xl'):
            ui.label('Welcome to Bellyns Ushering Hub').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('Making Every Event Memorable & Seamless').classes('text-xl text-center text-gray-600 mb-6')
            
            # Hero image
            ui.image('/assets/ushers2.jpg.JPEG').classes('w-full h-auto rounded-lg shadow-lg mb-6').style('max-height: none; object-fit: scale-down;')


            
            with ui.row().classes('w-full justify-center gap-4'):
                ui.button('Book Our Services', on_click=lambda: ui.navigate.to('/contact')).classes('bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-lg font-semibold')
                ui.button('View Gallery', on_click=lambda: ui.navigate.to('/gallery')).classes('bg-yellow-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold')
        
        # Services overview
        with ui.row().classes('w-full gap-6 mt-8'):
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('celebration', size='3rem').classes('text-purple-600 mb-4')
                ui.label('Weddings').classes('text-xl font-bold mb-2')
                ui.label('Professional ushering for your special day').classes('text-gray-600')
            
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('business', size='3rem').classes('text-blue-600 mb-4')
                ui.label('Corporate Events').classes('text-xl font-bold mb-2')
                ui.label('Seamless guest management for business functions').classes('text-gray-600')
            
            with ui.card().classes('flex-1 p-6 hover:shadow-lg transition-shadow'):
                ui.icon('party_mode', size='3rem').classes('text-green-600 mb-4')
                ui.label('Private Parties').classes('text-xl font-bold mb-2')
                ui.label('Friendly service for memorable celebrations').classes('text-gray-600')
        
        # Why choose us section
        with ui.card().classes('w-full p-8 mt-8'):
            ui.label('Why Choose Our Ushering Service?').classes('text-2xl font-bold text-center mb-6')
            with ui.row().classes('w-full gap-8'):
                with ui.column().classes('flex-1'):
                    ui.icon('verified', size='2rem').classes('text-green-600 mb-2')
                    ui.label('Experienced Team').classes('font-bold mb-2')
                    ui.label('Our professional ushers have years of experience in event management')
                
                with ui.column().classes('flex-1'):
                    ui.icon('schedule', size='2rem').classes('text-blue-600 mb-2')
                    ui.label('Reliable & Punctual').classes('font-bold mb-2')
                    ui.label('We arrive on time and ensure smooth event flow from start to finish')
                
                with ui.column().classes('flex-1'):
                    ui.icon('favorite', size='2rem').classes('text-red-600 mb-2')
                    ui.label('Personalized Service').classes('font-bold mb-2')
                    ui.label('Tailored solutions to meet your specific event requirements')