from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class StudentgradesModel(db.Model):
    __tablename__ = "table"
 
    Grades= db.Column(db.integer, primary_key=True)
    Scores = db.Column(db.models.Text()unique = True)
   Fullnames = db.Column(db.String())
   MathScore = db.Column(db.Integer())
   EnglishScore = db.Column(db.Integer())
   KiswahiliScore = db.Column(db.Integer())
   ScienceScore = db.Column(db.Integer())
   CREScore = db.Column(db.Integer())
   # position = db.Column(db.String(80))
 
    def __init__(self, Grades,Fullnames,MathScore,EnglishScore,KiswahiliScore,ScienceScore,CREScore):
        self.Grades= Grades
        self.Fullnames = Fullnames
        self.MathScore = MathScore
        self.EnglishScore = EnglishScore
        self.KiswahiliScore = KiswahiliScore
        self.ScienceScore = ScienceScore
        self.CREScore = CREScore
        #self.position = position
 
    def __repr__(self):
        return f"{self.Fullname}:{self.Grades}"
    