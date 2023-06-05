
import sqlite3

class dimDate:
    def __init__(self):
        self.conn = sqlite3.connect("database/moneyTracker.db")
        self.cur = self.conn.cursor()
        
        
        
    def runStatement(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
        
    def createTable(self):
        createStatement = """
            CREATE TABLE IF NOT EXISTS DimDate AS
            -- Initiate the recursive loop
            WITH RECURSIVE
            -- Define a CTE to hold the recursive output
            rDateDimensionMinute (CalendarDateInterval)
            AS
                (
                    -- The anchor of the recursion is the start date of the date dimension
                    SELECT datetime('2015-04-01 00:00:00')
                    UNION ALL
                    -- The recursive query increments the time interval by the desired amount
                    -- This can be any time increment (monthly, daily, hours, minutes)
                    SELECT datetime(CalendarDateInterval, '+24 hour') FROM rDateDimensionMinute
                    -- Set the number of recursions
                    -- Functionally, this is the number of periods in the date dimension
                    LIMIT 100000
                )
            -- Output the result set to the permanent table
            SELECT 
                strftime('%Y%m%d',CalendarDateInterval)	Id,
                CalendarDateInterval,
                datetime(CalendarDateInterval, '+86399 second') CalendarDateIntervalEnd,
                strftime('%w',CalendarDateInterval)	DayNumber,
                CASE cast (strftime('%w', CalendarDateInterval) as integer)
                    WHEN 0 THEN 'Sunday'
                    WHEN 1 THEN 'Monday'
                    WHEN 2 THEN 'Tuesday'
                    WHEN 3 THEN 'Wednesday'
                    WHEN 4 THEN 'Thursday'
                    WHEN 5 THEN 'Friday'
                    WHEN 6 THEN 'Saturday' END DayOfWeek,
                substr('SunMonTueWedThuFriSat', 1 + 3*strftime('%w', CalendarDateInterval), 3) DayOfWeekAbbr,
                strftime('%d',CalendarDateInterval)	DayOfMonth,
                CASE cast (strftime('%w', CalendarDateInterval) as integer)
                    WHEN 0 THEN 1
                    WHEN 6 THEN 1
                    ELSE 0 END IsWeekend,
                CASE cast (strftime('%w', CalendarDateInterval) as integer)
                    WHEN 0 THEN 0
                    WHEN 6 THEN 0
                    ELSE 1 END IsWeekday,
                strftime('%m',CalendarDateInterval)	MonthNumber,
                CASE strftime('%m', date(CalendarDateInterval)) 
                    WHEN '01' THEN 'January' 
                    WHEN '02' THEN 'Febuary' 
                    WHEN '03' THEN 'March' 
                    WHEN '04' THEN 'April' 
                    WHEN '05' THEN 'May' 
                    WHEN '06' THEN 'June' 
                    WHEN '07' THEN 'July' 
                    WHEN '08' THEN 'August' 
                    WHEN '09' THEN 'September' 
                    WHEN '10' THEN 'October' 
                    WHEN '11' THEN 'November' 
                    WHEN '12' THEN 'December' ELSE '' END MonthName,
                CASE strftime('%m', date(CalendarDateInterval)) 
                    WHEN '01' THEN 'Jan' 
                    WHEN '02' THEN 'Feb' 
                    WHEN '03' THEN 'Mar' 
                    WHEN '04' THEN 'Apr' 
                    WHEN '05' THEN 'May' 
                    WHEN '06' THEN 'Jun' 
                    WHEN '07' THEN 'Jul' 
                    WHEN '08' THEN 'Aug' 
                    WHEN '09' THEN 'Sep' 
                    WHEN '10' THEN 'Oct' 
                    WHEN '11' THEN 'Nov' 
                    WHEN '12' THEN 'Dec' ELSE '' END MonthAbbr,
                strftime('%Y',CalendarDateInterval)	YearNumber
            FROM rDateDimensionMinute;
        """
        self.runStatement(createStatement)