from app import app, db
from app.models import WordClass, DuolingoWord

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'WordClass': WordClass,
            'DuolingoWord': DuolingoWord}
