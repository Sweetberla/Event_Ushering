from nicegui import ui
from .navigation import create_navigation

def gallery():
    create_navigation()
    
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section
        with ui.card().classes('w-full p-8 text-center bg-gradient-to-r from-pink-50 to-purple-50'):
            ui.label('Our Work Gallery').classes('text-3xl font-bold text-gray-800 mb-4')
            ui.label('See Our Professional Ushering Services in Action').classes('text-lg text-gray-600')
        
        # Gallery categories
        with ui.row().classes('w-full gap-4 mt-8 justify-center'):
            ui.button('All Events', on_click=lambda: show_category('all')).classes('bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded-lg')
            ui.button('Weddings', on_click=lambda: show_category('weddings')).classes('bg-pink-600 hover:bg-pink-700 text-white px-6 py-2 rounded-lg')
            ui.button('Corporate', on_click=lambda: show_category('corporate')).classes('bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg')
            ui.button('Private Events', on_click=lambda: show_category('private')).classes('bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-lg')
            ui.button('Non-Profit', on_click=lambda: show_category('non-profit')).classes('bg-orange-600 hover:bg-orange-700 text-white px-6 py-2 rounded-lg')
        
        # Wedding gallery section
        with ui.card().classes('w-full p-6 mt-8'):
            ui.label('Wedding Events').classes('text-2xl font-bold text-pink-600 mb-4')
            with ui.row().classes('w-full gap-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/clientpic2.jpg').classes('w-full h-128 object-contain rounded-lg mb-3')
                    ui.label('Elegant Wedding Reception').classes('font-bold mb-2')
                    ui.label('Professional ushering for a 200-guest wedding celebration').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/clientpic1.jpg').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Elegant Wedding Ceremony').classes('font-bold mb-2')
                    ui.label('Outdoor ceremony coordination and guest guidance').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/clientpic3.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Elegant Wedding Ceremony').classes('font-bold mb-2')
                    ui.label('Cultural wedding with traditional protocols').classes('text-sm text-gray-600')
            
            with ui.row().classes('w-full gap-4 mt-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/clientpic2.jpg.JPEG').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Elegant Wedding Reception').classes('font-bold mb-2')
                    ui.label('Grand wedding reception with professional ushering services').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/clientpic4.jpg').classes('w-full h-96 object-contain rounded-lg mb-3')
                    ui.label('Elegant Wedding Celebration').classes('font-bold mb-2')
                    ui.label('Luxury wedding coordination and guest management').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/clientwork.jpg.JPEG').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Professional Wedding Service').classes('font-bold mb-2')
                    ui.label('Comprehensive wedding ushering and coordination services').classes('text-sm text-gray-600')
        
        # Corporate events section
        with ui.card().classes('w-full p-6 mt-6'):
            ui.label('Corporate Events').classes('text-2xl font-bold text-blue-600 mb-4')
            with ui.row().classes('w-full gap-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/corporate.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Corporate Conference').classes('font-bold mb-2')
                    ui.label('Professional ushering for corporate business events').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/corporate1.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Business Meeting').classes('font-bold mb-2')
                    ui.label('Executive event coordination and guest management').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/brandact.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Brand Activation').classes('font-bold mb-2')
                    ui.label('Dynamic brand experience and guest engagement').classes('text-sm text-gray-600')
            
            with ui.row().classes('w-full gap-4 mt-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/brandact1.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Brand Event').classes('font-bold mb-2')
                    ui.label('Interactive brand activation and coordination').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/brandact2.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Product Launch').classes('font-bold mb-2')
                    ui.label('Professional product launch event management').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/brandact3.jpg.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Brand Experience').classes('font-bold mb-2')
                    ui.label('Comprehensive brand activation services').classes('text-sm text-gray-600')
        
        # Private events section
        with ui.card().classes('w-full p-6 mt-6'):
            ui.label('Private Events').classes('text-2xl font-bold text-green-600 mb-4')
            with ui.row().classes('w-full gap-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/privateparty.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Private Party').classes('font-bold mb-2')
                    ui.label('Intimate party coordination and guest management').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/privateparty1.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Private Party').classes('font-bold mb-2')
                    ui.label('Special milestone celebration with professional service').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/privateparty3.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Private Party').classes('font-bold mb-2')
                    ui.label('Warm hospitality for private family celebrations').classes('text-sm text-gray-600')
            
            with ui.row().classes('w-full gap-4 mt-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/ushers5.jpg.JPEG').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Private Event Service').classes('font-bold mb-2')
                    ui.label('Professional ushering for exclusive private gatherings').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/ushers4.jpg.JPEG').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Private Event Coordination').classes('font-bold mb-2')
                    ui.label('Dedicated service for private celebrations and events').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/usher7.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Private Event Management').classes('font-bold mb-2')
                    ui.label('Comprehensive guest management for private functions').classes('text-sm text-gray-600')
        
        # Traditional ceremony section
        with ui.card().classes('w-full p-6 mt-6'):
            ui.label('Traditional Ceremony').classes('text-2xl font-bold text-orange-600 mb-4')
            with ui.row().classes('w-full gap-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/dowry.jpg.JPEG').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Traditional Ceremony').classes('font-bold mb-2')
                    ui.label('Cultural ceremonies with traditional protocols and customs').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/dowry.jpg').classes('w-full h-80 object-contain rounded-lg mb-3')
                    ui.label('Traditional Ceremony').classes('font-bold mb-2')
                    ui.label('Heritage events with proper ceremonial guidance').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/dowry2.jpg').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Traditional Ceremony').classes('font-bold mb-2')
                    ui.label('Religious and cultural event coordination').classes('text-sm text-gray-600')
        
        # Waiting staff section
        with ui.card().classes('w-full p-6 mt-6'):
            ui.label('Waiting Staff Services').classes('text-2xl font-bold text-indigo-600 mb-4')
            with ui.row().classes('w-full gap-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/waiter.jpg').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Professional Waiting Staff').classes('font-bold mb-2')
                    ui.label('Experienced waiters for elegant reception service').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/waiter2.jpg').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Professional Waiting Staff').classes('font-bold mb-2')
                    ui.label('Attentive service for special occasions').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/waiter3.jpg').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Professional Waiting Staff').classes('font-bold mb-2')
                    ui.label('Courteous reception service coordination').classes('text-sm text-gray-600')
            
            with ui.row().classes('w-full gap-4 mt-4'):
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/waiters.jpg.JPEG').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Professional Waiting Staff').classes('font-bold mb-2')
                    ui.label('Team service for large events and gatherings').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/waiters2.jpg.JPEG').classes('w-full h-64 object-contain rounded-lg mb-3')
                    ui.label('Professional Waiting Staff').classes('font-bold mb-2')
                    ui.label('Coordinated waiting service for premium events').classes('text-sm text-gray-600')
                
                with ui.card().classes('flex-1 p-4 hover:shadow-lg transition-shadow'):
                    ui.image('/assets/ushers.jpg.JPEG').classes('w-full h-96 object-contain rounded-lg mb-3')
                    ui.label('Professional Ushering Staff').classes('font-bold mb-2')
                    ui.label('Professional ushering and reception service management').classes('text-sm text-gray-600')
        
        # Testimonials from gallery
        with ui.card().classes('w-full p-8 mt-8 bg-gray-50'):
            ui.label('What Our Clients Say').classes('text-2xl font-bold text-center mb-6')
            with ui.row().classes('w-full gap-6'):
                with ui.card().classes('flex-1 p-6 bg-white'):
                    ui.label('"The ushers were incredibly professional and made our wedding day seamless. Our guests were so well taken care of!"').classes('italic mb-4')
                    ui.label('- Salomey & Nii Odoi, Wedding Clients').classes('font-bold text-purple-600')
                
                with ui.card().classes('flex-1 p-6 bg-white'):
                    ui.label('"Outstanding service for our corporate event. The team handled 300+ attendees with grace and efficiency."').classes('italic mb-4')
                    ui.label('- Jennifer K., Event Manager').classes('font-bold text-blue-600')
        
        # Call to action
        with ui.card().classes('w-full p-8 mt-8 text-center bg-gradient-to-r from-purple-600 to-blue-600 text-white'):
            ui.label('Ready to Make Your Event Memorable?').classes('text-2xl font-bold mb-4')
            ui.label('Contact us today to discuss your ushering needs').classes('text-lg mb-6')
            ui.button('Get a Quote', on_click=lambda: ui.navigate.to('/contact')).classes('bg-white text-purple-600 hover:bg-gray-100 px-8 py-3 rounded-lg font-semibold')

def show_category(category):
    # This function would filter gallery items by category
    # For now, it's a placeholder for future functionality
    ui.notify(f'Showing {category} events', type='info')