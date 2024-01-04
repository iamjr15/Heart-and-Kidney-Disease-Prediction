import warnings

from multipage import MultiPage
from pages import kidney,heart
warnings.filterwarnings("ignore")

app = MultiPage()

app.add_page("kidney",kidney.app)
app.add_page("heart", heart.app)

# The main app
app.run()
