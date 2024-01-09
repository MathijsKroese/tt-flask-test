import enum


class TaskType(enum.Enum):
    UPLOAD = "Upload Evidence"
    REVIEW = "Review Evidence"
    READ = "Read Document"
    SIGN = "Sign Document"


class TaskStatus(enum.Enum):
    COMPLETE = "Task Completed"
    INCOMPLETE = "Task Incomplete"
    PAUSE = "Task Paused"


class StepTypes(enum.Enum):
    DYEING = "dyeing"
    GINNING = "ginning"
    CONFECTIONING = "confectioning"
    PRINTING = "printing"
    CUTTING = "cutting"
    ACCESSORIES = "accessories"
    IMPORTING = "importing"
    SEWING = "sewing"
    ASSEMBLING = "assembling"
    WAREHOUSING = "warehousing"
    TANNING = "tanning"
    PACKING = "packing"
    FINISHING = "finishing"
    FABRIC_TRADING = "fabric trading"
    TRIMS = "trims"
    DESIGN_DEVELOPMENT = "design & development"
    YARN_TRADING = "yarn trading"
    RECYCLED_MATERIAL = "recycled material"
    MATERIAL_TRADING = "material trading"
    TRANSPORT = "transport"
    EXPORTING = "exporting"
    RETAILING = "retailing"
    MAN_MADE_MATERIAL = "man-made material"
    LABELLING = "labelling"

