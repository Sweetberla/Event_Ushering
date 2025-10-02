from nicegui import ui

def create_navigation():
    """Create a consistent navigation header for all pages"""
    with ui.header().classes('bg-yellow-500 text-black shadow-lg'):
        with ui.row().classes('w-full max-w-6xl mx-auto px-4 py-2 items-center'):
            with ui.column().classes('flex-1'):
                with ui.row().classes('items-center gap-4'):
                    ui.image('/assets/usheringlogo.jpg').classes('h-10 w-10 object-contain').style('filter: brightness(2) contrast(1.2);')
                    ui.label('BELLYNS USHERING HUB').classes('text-2xl font-bold uppercase')
            with ui.row().classes('gap-6'):
                ui.link('HOME', '/').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('ABOUT', '/about').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('SERVICES', '/services').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('GALLERY', '/gallery').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('TESTIMONIALS', '/testimonials').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('CONTACT', '/contact').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('FAQS', '/faqs').classes('text-black hover:text-purple-200 transition-colors uppercase')
                ui.link('INFO', '/footer').classes('text-black hover:text-purple-200 transition-colors uppercase')

