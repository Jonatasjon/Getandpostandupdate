#https://github.com/puentesarrin/pymongolab/blob/159a46c6cf88313c11522503d9243e2e16d3d72c/doc/examples.rst

from pymongolab import MongoClient


count=0
INT1=0
PEDS=0
TAXA1=0
i=0


# Read equipments
con = MongoClient("t3md-y8OEJDs1vmPqIzuqfjqNUvckV12")
db = con.mco
col = db.equipments.find()
col_list=list(col)


# TIRA O HASH
# FAZER A CONEXAO DE NOVO COM O DE DADOS


for equipments in col_list:
 	print equipments["hash"]

        con = MongoClient(equipments["hash"])
	db = con.dados
	
	count=0

	for collection_name in list(db.collection_names()):
	    if collection_name != "system.indexes":
	    	print collection_name
	
		
	    	col = db[collection_name].find()
	    	col_list = list(col)
	    	#print col_list
		
     	 	
	    	#for collection_name in col_list:

  			#print collection_name["hash"]
		print "soma da taxa por banco",[TAXA1]
		print "soma da interacoes por banco",[INT1]
		print "soma da pedestres por banco",[PEDS]

		for document in col_list:
    			    print document["_id"]
    
    
    			    print "Interacoes:", document["Interacoes"]
    		 	    print "Pedestres:",  document["Pedestres"]
    			    print "Taxa:",  document["Taxa"]
    			    a = float( document["Taxa"]) 
   			    b = float( document["Interacoes"])
    			    c = float( document["Pedestres"])
  
    			    TAXA1 = a+ TAXA1
   			    INT1 = b + INT1
    			    PEDS = c + PEDS


    			    count+=1
		print "contagem",[count]


	TAXA1=TAXA1/count
	INT1=INT1/count
	PEDS=PEDS/count

print "media interacoes",[INT1]
print "media pedestres",[PEDS]
print "meida taxa",[TAXA1]



# POST VALUES  AND  UPDATE
con.mco.equipments.update({"id":"1"} , {"$set": { "interacoes": str(INT1), "pedestres": str(PEDS), "taxa": str(TAXA1)}}, upsert=True,   multi=True);

