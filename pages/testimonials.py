from nicegui import ui
from .navigation import create_navigation

def testimonials():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section with background image
        with ui.card().classes('w-full p-8 text-center relative overflow-hidden').style('background-image: url("/assets/clientpic2.jpg"); background-size: cover; background-position: center;'):
            # Light overlay for text readability
            ui.element('div').classes('absolute inset-0 bg-black opacity-40')
            # Content on top of overlay
            with ui.column().classes('relative z-10'):
                ui.label('Client Testimonials').classes('text-3xl font-bold text-white mb-4 drop-shadow-lg')
                ui.label('Hear What Our Satisfied Clients Have to Say').classes('text-lg text-white drop-shadow-lg')
        
        # Featured testimonials
        with ui.row().classes('w-full gap-6 mt-8'):
            with ui.card().classes('flex-1 p-6 bg-white shadow-lg'):
                with ui.row().classes('items-center mb-4'):
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                ui.label('"Absolutely exceptional service! The ushers were professional, friendly, and made our wedding day run smoothly. Our guests were impressed with their attention to detail and warm hospitality."').classes('italic text-lg mb-4')
                ui.label('Miriam & Charles ').classes('font-bold text-black')
                ui.label('Wedding - February 2025').classes('text-sm text-black')
            
            with ui.card().classes('flex-1 p-6 bg-white shadow-lg'):
                with ui.row().classes('items-center mb-4'):
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                    ui.icon('star', size='1.5rem').classes('text-yellow-500')
                ui.label('"Outstanding coordination for our corporate conference. The team managed 400+ attendees flawlessly. Professional, punctual, and incredibly organized. Highly recommended!"').classes('italic text-lg mb-4')
                ui.label('Mawuena').classes('font-bold text-black')
                ui.label('Send-Off Party -August 2024').classes('text-sm text-black')
        
        # More testimonials grid
        with ui.row().classes('w-full gap-6 mt-6'):
            with ui.card().classes('flex-1 p-6'):
                with ui.row().classes('items-center mb-3'):
                    for _ in range(5):
                        ui.icon('star', size='1.2rem').classes('text-yellow-500')
                ui.label('"The ushers made my Fathers anniversary celebration perfect. They anticipated our needs and ensured every guest felt welcome and comfortable."').classes('italic mb-3')
                ui.label('Angela Bannerman').classes('font-bold text-black text-sm')
                ui.label('50th Anniversary Celebration').classes('text-xs text-black')
            
            with ui.card().classes('flex-1 p-6'):
                with ui.row().classes('items-center mb-3'):
                    for _ in range(5):
                        ui.icon('star', size='1.2rem').classes('text-yellow-500')
                ui.label('"Incredible service for our Football gala. The team handled VIP guests with grace and maintained perfect protocol throughout the evening."').classes('italic mb-3')
                ui.label('Nene').classes('font-bold text-black text-sm')
                ui.label('Wormanne Arts Festival -September 2025').classes('text-xs text-black')
            
            with ui.card().classes('flex-1 p-6'):
                with ui.row().classes('items-center mb-3'):
                    for _ in range(5):
                        ui.icon('star', size='1.2rem').classes('text-yellow-500')
                ui.label('"Professional, courteous, and efficient. They made our event seamless and allowed us to focus on our memorable day."').classes('italic mb-3')
                ui.label('Madam Emelia').classes('font-bold text-black text-sm')
                ui.label('Funeral - September 2025').classes('text-xs text-black')
        
        # Statistics section
        with ui.card().classes('w-full p-8 mt-8 bg-yellow-600'):
            ui.label('Our Track Record').classes('text-2xl font-bold text-center mb-6')
            with ui.row().classes('w-full gap-8 text-center'):
                with ui.column().classes('flex-1'):
                    ui.label('50+').classes('text-4xl font-bold text-black')
                    ui.label('Events Served').classes('text-lg text-black')
                
                with ui.column().classes('flex-1'):
                    ui.label('98%').classes('text-4xl font-bold text-black')
                    ui.label('Client Satisfaction').classes('text-lg text-black')
                
                with ui.column().classes('flex-1'):
                    ui.label('3 Years').classes('text-4xl font-bold text-black')
                    ui.label('Experience').classes('text-lg text-black')
                
                with ui.column().classes('flex-1'):
                    ui.label('24/7').classes('text-4xl font-bold text-black')
                    ui.label('Support Available').classes('text-lg text-black')
        
        # More detailed testimonials
        with ui.card().classes('w-full p-8 mt-8'):
            ui.label('Detailed Client Experiences').classes('text-2xl font-bold mb-6')
            
            with ui.card().classes('w-full p-6 mb-6 bg-gray-50'):
                ui.label('Wedding Reception - 250 Guests').classes('text-lg font-bold text-pink-600 mb-3')
                ui.label('"From the initial consultation to the end of our reception, the ushering team was phenomenal. They coordinated with our wedding planner, managed the guest seating perfectly, and even helped with some last-minute changes. Our elderly guests especially appreciated their attentiveness and assistance. The team was dressed impeccably and blended seamlessly with our wedding aesthetic. We couldn\'t have asked for better service!"').classes('italic mb-4')
                ui.label('- Maame & Paa, November 2024').classes('font-bold')
            
            with ui.card().classes('w-full p-6 mb-6 bg-gray-50'):
                ui.label('Corporate Annual Meeting - 200 Attendees').classes('text-lg font-bold text-blue-600 mb-3')
                ui.label('"Managing a large corporate event requires precision and professionalism, and this team delivered both in spades. They handled registration, guided attendees to breakout sessions, managed VIP areas, and coordinated with our AV team flawlessly. Their multilingual capabilities were particularly valuable for our international guests. The feedback from our executives was overwhelmingly positive."').classes('italic mb-4')
                ui.label('- Thomas Anderson, CEO - Global Enterprises').classes('font-bold')
        
        # Call to action
        with ui.card().classes('w-full p-8 mt-8 text-center bg-black text-white'):
            ui.label('Join Our Satisfied Clients').classes('text-2xl  text-yellow-600 font-bold mb-4')
            ui.label('Experience the difference professional ushering makes').classes('text-lg  text-yellow-600 mb-6')
            with ui.row().classes('gap-4 justify-center'):
                ui.button('Book Our Services', on_click=lambda: ui.navigate.to('/contact')).classes('bg-yellow-600 text-yellow-600 hover:bg-yellow-600 px-8 py-3 rounded-lg font-semibold')
                ui.button('View Our Services', on_click=lambda: ui.navigate.to('/services')).classes('bg-yellow-600 text-yellow-600 hover:bg-yellow-600  px-8 py-3 rounded-lg font-semibold')