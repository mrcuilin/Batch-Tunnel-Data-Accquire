initRetryTimesLimit = 3

COM_PORT = "/dev/ttyUSB0"
COM_BAUD = 9600

LOG_LEVEL = "INFO"

INIT_CMD = "@\r\n"
SHOW_MSG_CMD = "D \"%S\"\r\n"
SHOW_DEFAULT_CMD = "DW\r\n"
WEIGHT_CMD = "S\r\n"
TARE_CMD="TA\r\n"

DB_SPEC = ["localhost","3306","root","","serialdata"]


SAMPLE_INTERVAL = 3
ENABLED = False
RUNNING = False
CURRENT_SESSION = None
