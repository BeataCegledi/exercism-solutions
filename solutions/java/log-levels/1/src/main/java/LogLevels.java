public class LogLevels {
    
    public static String message(String logLine) {
        int index = logLine.indexOf(": ");
        String msg = logLine.substring(index + 2);
        return msg.trim(); 
    }

    public static String logLevel(String logLine) {
        int start = logLine.indexOf("[") + 1;
        int end = logLine.indexOf("]"); 
        String level = logLine.substring(start, end);
        return level.toLowerCase(); 
    }

    public static String reformat(String logLine) {
        return (message(logLine) + " (" + logLevel(logLine) + ")");
    }
}
