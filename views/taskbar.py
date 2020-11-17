import aiohttp_jinja2


def web_render(request):
    return aiohttp_jinja2.render_template('templates/taskbar.html', request, {})
