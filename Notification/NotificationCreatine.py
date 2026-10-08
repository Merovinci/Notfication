from pathlib import Path
from winotify import Notification

toast = Notification(
    app_id="Python Application",
    title="Já tomou a creatina?",
    msg="Além da creatina, não se esqueça das 100 flexoes, abraços!",
    duration="short",
    icon=str(Path(__file__).with_name("creatina.png")),
)
toast.show()