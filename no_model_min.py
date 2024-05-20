from ulab import numpy as np
def _relu(x):
	return np.maximum(0,x)
def _sigmoid(x):
	return 1/(1+np.exp(-x))
def _layer_zero(input_data):
	w0=np.array([[-4.97591466e-01,-3.48154902e-01,-9.64563787e-02,-4.40266915e-02,5.13613582e-01,-6.10522591e-02,-3.47615294e-02,2.88594782e-01,-8.85496065e-02,2.12527990e-01,3.30001622e-01,7.58453384e-02],[-1.27492115e-01,4.95373383e-02,-1.57608762e-01,-4.92550097e-02,-7.41389468e-02,1.77854940e-01,1.98510706e-01,2.09193066e-01,-7.28763118e-02,9.65496376e-02,-7.77478367e-02,-9.66457278e-02],[1.06221072e-01,7.24562407e-02,2.04165325e-01,-7.58996159e-02,4.90117222e-02,-1.36507004e-01,-6.86904788e-02,1.85969453e-02,-1.41062304e-01,7.45521039e-02,1.33563578e-01,3.82802659e-03],[-8.52456763e-02,2.53689200e-01,-2.39008814e-02,1.94278255e-01,-2.69632757e-01,1.31557286e-01,-2.69171060e-03,1.76334307e-01,-1.33269429e-01,-2.20754936e-01,1.06023289e-01,2.43034512e-01],[2.28796661e-01,8.57962593e-02,-6.07645214e-02,-1.36777923e-01,-1.02011338e-01,-2.44704083e-01,2.28717878e-01,-2.07664315e-02,6.01623394e-02,-1.09244689e-01,1.13376960e-01,5.31305224e-02],[-1.49923503e-01,5.40319309e-02,2.76568979e-01,6.85752034e-02,1.37822792e-01,-1.36446223e-01,2.75661089e-02,-6.96043745e-02,8.00784677e-02,4.72860597e-02,-5.72931115e-03,-1.09331116e-01],[7.63551071e-02,-2.01310366e-01,6.90016709e-03,2.96932578e-01,9.26339552e-02,3.50874662e-02,1.24513488e-02,2.53022045e-01,-1.45443067e-01,-1.11637279e-01,-2.93283956e-05,-1.28838167e-01],[2.08078343e-02,-1.27906993e-01,1.40025541e-01,8.70746523e-02,-3.86649603e-03,2.75576245e-02,1.29678071e-01,7.90816918e-02,1.48384586e-01,-1.12928234e-01,2.14731600e-02,2.46492818e-01],[-2.68742368e-02,-7.25817233e-02,1.70269638e-01,-6.74946606e-02,-9.64430273e-02,1.97632000e-01,4.37725373e-02,2.24634647e-01,-9.60620418e-02,-1.10878691e-01,3.12824361e-02,8.61454979e-02],[2.13755235e-01,1.99725121e-01,-1.48769785e-02,-1.62346587e-01,-6.99169338e-02,6.64472058e-02,-1.06776608e-02,1.26448184e-01,-3.65157157e-01,6.87637031e-02,-1.51696905e-01,4.44301218e-02],[2.21566811e-01,-9.31609496e-02,9.17831659e-02,2.08272249e-01,4.88626212e-02,-1.04722701e-01,-1.05342060e-01,-5.49319871e-02,-1.22663617e-01,-1.30428895e-01,-3.10298800e-02,1.23200379e-01],[-1.33388475e-01,1.69885203e-01,-3.63785960e-02,7.98837617e-02,1.74949411e-03,1.46997184e-01,-3.92615974e-01,6.48709387e-02,-2.63804287e-01,7.34840930e-02,-1.53784797e-01,3.17909628e-01],[-1.54809460e-01,2.68280655e-01,1.37583271e-01,1.03114493e-01,-2.63132509e-02,1.78944036e-01,4.48270403e-02,2.13879585e-01,-1.73378274e-01,-6.08024448e-02,-1.40879855e-01,-4.25300561e-02],[-1.34938553e-01,-4.84419502e-02,3.40939648e-02,1.84744149e-01,-2.72330254e-01,-1.78654537e-01,5.73407188e-02,1.29591092e-01,-2.15156525e-01,-1.17826439e-01,-2.19659060e-01,-1.20152488e-01],[6.06940761e-02,-2.03321408e-02,-7.27882385e-02,2.08977237e-01,-1.88799575e-02,7.17384145e-02,1.78676009e-01,-5.66789657e-02,9.82583910e-02,-2.26157069e-01,-7.77398497e-02,-2.33672872e-01],[2.68916875e-01,7.65278637e-02,8.93844739e-02,1.47371888e-01,3.05777848e-01,-8.22771788e-02,-9.87015292e-02,2.83623725e-01,-1.25272602e-01,8.54255334e-02,-1.82457268e-01,2.00247794e-01],[-1.50934026e-01,-1.25254720e-01,-4.88218009e-01,-3.23920488e-01,2.38912597e-01,3.21868271e-01,-5.81769608e-02,6.74387962e-02,-1.21145807e-01,3.78832877e-01,1.60731912e-01,-1.28496408e-01],[3.66435617e-01,1.38609931e-01,-1.40166044e-01,-1.75830096e-01,2.67599165e-01,-4.49557081e-02,1.88275307e-01,4.64328341e-02,3.01892310e-01,7.79502443e-06,-1.07656427e-01,2.73387805e-02],[3.96858864e-02,-1.95369553e-02,-3.78224373e-01,-1.10172950e-01,1.37235045e-01,-1.10199889e-02,1.22827195e-01,2.51732431e-02,2.88845092e-01,1.54470786e-01,4.95812520e-02,9.68530402e-02],[-1.77407920e-01,3.35215300e-01,-6.64436966e-02,-5.28201982e-02,-3.11636388e-01,-1.18662659e-02,-9.22466069e-02,1.55326203e-01,-3.74499671e-02,6.63819611e-02,1.35921091e-02,-1.67969137e-01],[-3.00518781e-01,-4.08031270e-02,5.08502834e-02,-5.46384007e-02,5.07085994e-02,1.75255701e-01,1.00928307e-01,8.81417170e-02,2.52746623e-02,-1.55042544e-01,6.17961287e-02,-6.74463287e-02],[-2.73041666e-01,5.31119518e-02,1.44233312e-02,-3.12938280e-02,-1.41446277e-01,-6.11292310e-02,-1.63170025e-01,1.32249966e-01,-1.97827015e-02,4.34016399e-02,-1.63343892e-01,4.95858043e-02],[1.80105120e-01,-1.38527021e-01,1.33175910e-01,-6.06347434e-02,9.63696167e-02,-4.45689783e-02,-1.48434371e-01,1.94733709e-01,1.53649688e-01,1.09688520e-01,-6.07350208e-02,-1.23088874e-01],[-1.39569581e-01,-2.99566947e-02,2.36185282e-01,1.59565046e-01,1.32984832e-01,-9.71393660e-02,1.81482449e-01,1.22638695e-01,-2.71068662e-01,-1.07634492e-01,-9.59608480e-02,-2.07147390e-01],[2.39953306e-03,4.84044068e-02,-9.32793394e-02,1.01557665e-01,-7.95148984e-02,-1.89224467e-01,6.40991852e-02,-1.87834546e-01,1.97486326e-01,-3.25080343e-02,-2.95529455e-01,-1.60612255e-01],[-6.92793503e-02,1.89327472e-03,-1.32652104e-01,3.92031902e-03,1.27854139e-01,1.03263207e-01,-1.43438801e-01,1.46077663e-01,-2.47993499e-01,-2.36500278e-02,1.42356426e-01,-1.49148302e-02],[-1.63655102e-01,-6.05586506e-02,1.85286850e-02,-1.35026127e-01,-1.98037595e-01,-1.37843952e-01,-2.22297803e-01,-1.36897773e-01,-6.68235272e-02,1.97197661e-01,3.65024656e-02,-2.51021143e-03],[-1.04702219e-01,1.09398760e-01,-6.62717642e-03,2.79187802e-02,6.54522423e-03,2.94418409e-02,-1.61232650e-01,3.24893355e-01,-2.80570924e-01,-3.11269090e-02,4.67298478e-02,5.19966967e-02],[1.57862484e-01,-3.16926949e-02,2.25922048e-01,-1.01695716e-01,2.24846210e-02,1.03593310e-02,-6.38246164e-02,1.96833029e-01,-2.14736387e-02,-6.84522316e-02,-1.04298651e-01,9.96224731e-02],[4.52542119e-02,1.48411226e-02,1.07491082e-02,-3.04489136e-02,-1.25700101e-01,-9.21508968e-02,-6.37167245e-02,-1.85922921e-01,-3.09527293e-02,-1.38430312e-01,-5.19680977e-02,9.11164284e-02],[1.40995741e-01,-6.85577244e-02,-1.76125661e-01,-7.62400124e-03,-2.34641016e-01,6.41739443e-02,-1.22507952e-01,-1.20696574e-01,-1.27948225e-01,-6.54283352e-03,-5.91017865e-02,1.04756087e-01],[9.47208032e-02,1.17200769e-01,-1.27780542e-01,-1.91708133e-01,-2.34830920e-02,1.50274262e-01,-7.43753687e-02,1.71171948e-01,-6.70370366e-03,3.61375064e-02,-1.61509454e-01,-7.94264674e-03],[1.42531753e-01,5.70578277e-02,-1.24608599e-01,-4.09085415e-02,5.01040593e-02,1.45906806e-01,-5.19348457e-02,1.06332779e-01,2.26112500e-01,3.44893247e-01,-2.84265697e-01,3.10821235e-01],[7.44539425e-02,-2.04106010e-02,-1.47083253e-01,-8.60040542e-03,7.98827261e-02,-3.97767961e-01,3.89664099e-02,-1.33053809e-01,1.99599475e-01,2.03787521e-01,-4.30167884e-01,-1.05337515e-01],[3.32720717e-03,-2.06010044e-01,-3.65893006e-01,-3.96728754e-01,2.75896519e-01,-4.97438014e-02,1.64612383e-01,1.59015164e-01,2.06077676e-02,-5.05484417e-02,1.28691643e-01,-2.16122717e-01],[-1.98634490e-01,9.71286446e-02,-1.17505446e-01,-2.46524885e-01,-1.36212230e-01,5.68437092e-02,1.47960827e-01,-2.00189039e-01,-7.78563926e-03,5.15755713e-02,1.16943344e-01,-2.50293165e-01],[-1.86962634e-01,7.84111321e-02,1.51692525e-01,7.98751712e-02,2.39935592e-02,-1.90676183e-01,1.41015619e-01,-1.54295012e-01,8.92912969e-02,2.14545503e-01,-4.35422063e-02,-1.42573401e-01],[-1.77738309e-01,4.49479550e-01,-1.98240146e-01,1.17363390e-02,1.19871765e-01,2.08887905e-01,-1.73471302e-01,-5.13319112e-03,2.92251557e-01,8.79372880e-02,-1.71290591e-01,-5.08017279e-02],[-7.81271458e-02,5.12380432e-03,-1.12892255e-01,7.04693794e-02,8.57724622e-02,-1.48953766e-01,1.73734426e-01,2.89074667e-02,2.52116621e-01,1.25549631e-02,-3.19414228e-01,-2.08443418e-01],[1.72526374e-01,2.14561760e-01,7.16423988e-02,1.13517106e-01,6.84149191e-02,1.33706048e-01,1.68162569e-01,-2.26497203e-01,1.92865375e-02,-9.38360244e-02,-8.16296116e-02,-4.25213389e-02],[1.75446793e-01,2.44856000e-01,2.51209557e-01,-1.39166847e-01,-2.52033994e-02,-2.41792768e-01,-8.26573893e-02,8.08227994e-03,6.93158358e-02,-2.93545634e-01,-2.83099771e-01,5.21511361e-02],[2.62451291e-01,1.39428619e-02,-8.13205168e-03,-1.80159405e-01,-3.95666033e-01,1.28747374e-01,1.21793769e-01,7.37043172e-02,5.25506213e-02,2.35786978e-02,1.00336615e-02,-1.32463992e-01],[-3.58301364e-02,1.39406547e-01,2.02325225e-01,7.76537433e-02,-4.59999219e-02,5.53081706e-02,-1.24649525e-01,-5.53931296e-02,1.04837321e-01,-5.94203807e-02,-1.47910893e-01,1.17649101e-01],[1.21364109e-01,-1.09520383e-01,-2.00209603e-01,1.80004500e-02,2.06133872e-01,-1.04786374e-01,-3.30783784e-01,-8.15214124e-03,1.45849958e-01,2.58504391e-01,-2.50266105e-01,1.48473665e-01],[2.18233079e-01,-1.48406103e-01,-3.97680067e-02,2.87065208e-02,-8.22364073e-03,6.50235638e-02,-5.15522622e-02,1.56664193e-01,1.17166445e-01,8.52282532e-03,-1.35104269e-01,4.72202373e-04],[9.69838202e-02,1.52858600e-01,-1.25984892e-01,1.87918427e-03,6.00773916e-02,2.30478525e-01,1.29315108e-01,-1.80469975e-01,1.40001088e-01,4.09839209e-03,9.14008170e-02,7.09111616e-02],[-8.75812098e-02,-2.77617741e-02,7.82851875e-02,1.63764432e-01,5.97253218e-02,-1.61060303e-01,2.31594453e-03,-1.58828378e-01,-8.91219825e-02,2.13468850e-01,-1.43276066e-01,6.75190166e-02],[1.14878401e-01,-4.52929735e-03,4.10063602e-02,1.19517304e-01,-1.79806620e-01,8.66799615e-03,2.24185839e-01,-9.27994773e-02,1.66489799e-02,-2.52896398e-02,1.34809613e-01,-2.32599005e-01],[-5.73596478e-01,-6.97025955e-02,3.61508787e-01,1.53952941e-01,-3.82826515e-02,-2.14134187e-01,1.14924960e-01,1.51688248e-01,2.05234692e-01,2.48194009e-01,-8.43097270e-02,2.36093625e-01],[-2.33697206e-01,1.41598046e-01,-1.26828089e-01,-9.33832228e-02,1.24591604e-01,-4.62374419e-01,2.11109713e-01,5.30887507e-02,2.96698153e-01,1.23085059e-01,1.65292829e-01,-2.83908658e-02],[-2.76143789e-01,-1.99759349e-01,-1.21232346e-01,-1.58935398e-01,2.03709200e-01,-1.68326795e-01,1.93017393e-01,-9.20716301e-03,-1.29126944e-03,1.35495991e-01,2.10401490e-01,-1.27300099e-01],[-5.05794346e-01,-5.39870679e-01,-9.54457298e-02,1.09634623e-02,1.13905907e-01,1.44860253e-01,5.61545566e-02,-1.81756169e-01,3.35137397e-01,-2.37725571e-01,4.76763844e-01,3.92116569e-02],[-4.60749753e-02,-3.31467479e-01,-1.97224066e-01,-2.19903395e-01,2.52518982e-01,1.13311499e-01,2.06806898e-01,1.98852420e-01,-3.11499238e-02,1.17216418e-02,1.82411730e-01,-1.59365833e-01],[-1.32926553e-01,-1.35055333e-01,-2.13669807e-01,3.66000235e-02,-1.18605793e-01,1.17512904e-01,-1.03250891e-01,-1.60290357e-02,1.02578335e-01,2.27585390e-01,-2.63532363e-02,1.40865162e-01],[-5.42520210e-02,3.00796270e-01,-5.28437383e-02,3.01729262e-01,1.66102946e-01,-4.09579366e-01,6.02073632e-02,-1.50648057e-01,2.28513241e-01,-5.58926314e-02,-3.90100293e-02,3.72968018e-01],[-9.78664383e-02,1.31806478e-01,-1.99426990e-03,1.88088089e-01,-2.20324650e-01,-4.25514393e-03,2.49072388e-01,-4.92450595e-02,2.03913748e-01,-1.28772050e-01,-1.92938209e-01,1.17477462e-01],[-4.73773628e-02,2.28259817e-01,-3.93591560e-02,-4.82419580e-02,-3.00430089e-01,-3.70859839e-02,2.23874241e-01,-1.41826361e-01,-1.08391762e-01,-2.89246105e-02,-9.63481590e-02,2.31095999e-01],[-4.56069037e-02,1.14149362e-01,-2.22378373e-01,1.21920869e-01,-6.45258054e-02,-6.36401698e-02,2.90083021e-01,3.07027269e-02,-2.13121492e-02,5.28156944e-02,-2.87014127e-01,-8.87435582e-03],[-1.47242472e-01,2.46135846e-01,-1.31916791e-01,2.71758940e-02,1.22206256e-01,4.90450338e-02,1.89996674e-03,1.77321076e-01,-1.46481186e-01,-1.11511469e-01,1.09189920e-01,1.95614249e-02],[-4.34003472e-02,-2.16842201e-02,1.87203363e-01,-7.40722492e-02,3.59404087e-02,1.01769827e-02,-1.96807325e-01,7.67783225e-02,2.40557939e-01,2.53264941e-02,-4.86410022e-01,9.74500328e-02],[7.27817416e-02,2.95196444e-01,-9.93270949e-02,1.70460641e-01,1.47877574e-01,1.78543493e-01,1.06669836e-01,1.68406636e-01,1.22546181e-01,-7.71408007e-02,-5.66195995e-02,1.24755122e-01],[-4.39378154e-03,8.18162188e-02,9.77641046e-02,2.05783635e-01,2.00339049e-01,2.23388046e-01,-9.16859601e-03,2.66449481e-01,-7.52744377e-02,-2.07280535e-02,-2.58182827e-02,-1.70794781e-02],[6.77610263e-02,1.57622352e-01,-1.06936730e-01,-1.20379433e-01,-3.03955209e-02,2.10272178e-01,1.17009871e-01,-7.61106052e-03,1.62283093e-01,-2.03837901e-01,-6.63709939e-02,-5.43173077e-03],[3.27208251e-01,9.27456394e-02,-1.56972542e-01,1.13489762e-01,1.90802161e-02,2.69062281e-01,-1.15631938e-01,7.76609732e-03,1.18501239e-01,-2.47247890e-01,-1.81455314e-01,1.17300674e-01],[-3.73159409e-01,1.17412679e-01,3.04190248e-01,1.43948764e-01,-1.70587867e-01,-1.17368326e-01,2.95157880e-01,-2.21087188e-01,3.26672643e-01,8.41975287e-02,-7.92723671e-02,-1.36562839e-01],[1.35542139e-01,2.70575374e-01,1.68189276e-02,-1.61731645e-01,2.97403663e-01,-2.72934020e-01,-1.69657409e-01,-1.40778035e-01,3.73258919e-01,1.38975680e-01,1.98803879e-02,-1.75646186e-01],[1.86710507e-01,-5.20145753e-03,-6.50531501e-02,7.56213292e-02,2.59330302e-01,-1.08405054e-01,-4.11343481e-03,1.59447089e-01,4.95194383e-02,-4.93462048e-02,5.66637442e-02,3.05007696e-01],[-6.44045919e-02,-4.46692675e-01,-1.20974429e-01,-2.63955653e-01,8.22263137e-02,4.33904052e-01,2.62123674e-01,9.87011269e-02,-1.14973970e-01,9.77714583e-02,1.12991892e-01,-1.55971169e-01],[7.80725479e-02,-4.31458682e-01,2.29300946e-01,1.64219514e-01,2.19887748e-01,3.87701988e-01,1.20738752e-01,3.88892800e-01,5.12204394e-02,1.46910856e-02,2.87304789e-01,8.91363248e-02],[-8.83833617e-02,-1.23705797e-01,1.78807959e-01,2.43950427e-01,-1.32437021e-01,-1.70186862e-01,2.14236885e-01,2.70014796e-02,1.94840387e-01,1.46848485e-01,1.93262950e-01,-1.17334202e-01],[-1.21875606e-01,-7.16379890e-03,2.80985475e-01,2.85298377e-01,-1.30089998e-01,6.34016320e-02,3.50995570e-01,7.60102943e-02,1.38227731e-01,-2.10854903e-01,1.16087593e-01,5.38279749e-02],[3.88402417e-02,7.34609812e-02,8.31576362e-02,-1.48777962e-01,-2.14216173e-01,6.07499331e-02,2.78944641e-01,3.01360004e-02,4.45351154e-01,-2.78755605e-01,1.43699506e-02,2.07712695e-01],[-1.24055715e-02,1.70507133e-01,1.97447047e-01,-1.26489863e-01,-8.34711790e-02,-8.67846161e-02,2.37766176e-01,8.62863362e-02,2.91972011e-02,-1.19765192e-01,1.79371312e-01,-4.11667302e-03],[-3.60281095e-02,7.56678879e-02,-1.15249962e-01,2.75547713e-01,1.33377776e-01,3.27632166e-02,-1.06239513e-01,7.18928054e-02,1.09423101e-01,1.60762519e-01,-1.78457443e-02,9.57903713e-02],[1.36778206e-01,-1.36695951e-02,-2.79530466e-01,7.50852600e-02,-1.72000438e-01,-1.21020123e-01,6.99729472e-02,1.45363599e-01,2.82081634e-01,9.93706211e-02,2.32142210e-02,7.29774535e-02],[-1.67155176e-01,2.15145290e-01,-4.92980182e-02,-2.37487648e-02,-1.34776816e-01,1.08764254e-01,-2.41675630e-01,1.59990013e-01,2.32608706e-01,-2.98371613e-02,-1.20079294e-01,4.48538363e-02],[-7.39213526e-02,6.01369552e-02,8.20812508e-02,-6.64456189e-03,7.01049417e-02,1.51207641e-01,-1.72187224e-01,2.12423846e-01,-1.13220988e-02,-8.99153296e-03,6.53213486e-02,5.95389046e-02],[-1.35284767e-01,1.80603638e-01,-1.15185417e-01,-6.05776384e-02,1.14662163e-02,1.81859791e-01,-2.76934862e-01,1.93205744e-01,-1.86383516e-01,1.38479337e-01,7.38940910e-02,2.16499314e-01],[-1.56401411e-01,-3.36785279e-02,7.13998526e-02,-8.96175802e-02,-8.51449892e-02,1.00779831e-01,-3.05001765e-01,4.31651324e-02,1.28438666e-01,-1.88655943e-01,-2.16057166e-01,1.65059000e-01],[2.45532244e-02,1.32468253e-01,-3.81766669e-02,-2.06435606e-01,1.57794535e-01,1.11098506e-01,-2.11024787e-02,1.92240849e-02,2.31626794e-01,3.87901776e-02,2.04773247e-01,1.72208503e-01],[2.56802468e-03,-3.10132325e-01,2.51825094e-01,3.05741876e-01,-5.23877621e-01,1.77289292e-01,1.96752280e-01,-4.09054935e-01,1.21943399e-01,3.64746898e-02,1.81897447e-01,-2.01886833e-01],[5.91137372e-02,-4.86255325e-02,-7.95978308e-02,-5.07899635e-02,1.28244206e-01,-7.44050816e-02,-2.71997064e-01,-4.90799686e-03,4.98279810e-01,-3.77450623e-02,-1.64020993e-03,-6.68835267e-02],[1.48970827e-01,4.97788042e-02,3.00582021e-01,8.30777660e-02,3.04112788e-02,-2.84438226e-02,-2.68173724e-01,9.62158740e-02,4.52736299e-03,2.97830164e-01,-2.23763864e-02,-1.60313360e-02],[6.90214336e-02,-2.75851101e-01,2.28984505e-01,1.51757270e-01,2.08928492e-02,3.68500501e-01,-1.25835627e-01,1.55207068e-01,-3.60695124e-01,-8.50854367e-02,-6.90980703e-02,2.23617539e-01],[-9.68661457e-02,-3.78032386e-01,2.16014370e-01,1.76944271e-01,-8.79569873e-02,4.49002236e-01,-8.40363503e-02,2.27069184e-01,-3.68328691e-01,5.78475138e-03,9.56924856e-02,1.33671463e-01],[1.08941734e-01,-1.95388973e-01,-2.50157136e-02,-1.46505594e-01,-1.08616389e-01,-4.08309288e-02,-1.72003359e-01,-9.84167233e-02,1.55043766e-01,4.10883576e-02,-3.89652736e-02,-8.54843706e-02],[-8.31417963e-02,-1.87603325e-01,-1.13739669e-02,-1.19145431e-01,-3.83551031e-01,-1.15255222e-01,-4.95920144e-03,-1.46607100e-03,1.34498984e-01,-2.57684499e-01,3.08402807e-01,1.28585234e-01],[1.24294767e-02,-2.36937236e-02,-2.55474091e-01,-1.46708056e-01,-2.73190111e-01,-1.88031152e-01,-1.52031243e-01,-1.34582236e-01,5.79407997e-02,-1.21190414e-01,2.61370599e-01,-8.02734271e-02],[2.32555464e-01,1.35482684e-01,-2.72533953e-01,-3.71493325e-02,3.29916067e-02,-6.89385459e-02,4.06391639e-03,1.02887452e-01,-1.70051143e-01,-1.09070607e-01,2.72722661e-01,2.92062700e-01],[-1.90189481e-02,6.36238307e-02,7.81011134e-02,2.40616798e-02,-1.49218708e-01,-1.34103462e-01,7.27865323e-02,6.87254667e-02,2.44363919e-01,-9.19330865e-02,1.94488883e-01,-7.68489242e-02],[3.83274746e-03,-1.74104959e-01,-1.53752521e-01,-1.27902418e-01,-6.74656630e-02,-9.19305757e-02,1.64710313e-01,1.28702477e-01,1.66928824e-02,-1.41322002e-01,5.98098487e-02,-1.08596310e-02],[-8.35176259e-02,-5.43321334e-02,-2.08866015e-01,-1.57140680e-02,-4.95328344e-02,-1.46177813e-01,-1.62071303e-01,6.20495118e-02,1.83022823e-02,1.04124993e-01,-2.12217420e-01,-1.63362250e-01],[-5.05597219e-02,-2.23609060e-01,2.87237585e-01,-1.12127759e-01,8.51145666e-03,-1.50429145e-01,1.11545742e-01,-1.41438052e-01,1.22826956e-01,1.84909523e-01,-1.81905359e-01,3.15361843e-02],[-6.02892004e-02,-1.90273970e-01,-4.57867421e-03,9.58193764e-02,-1.37332201e-01,-1.33287877e-01,3.26973125e-02,-8.92639682e-02,2.37100050e-01,-3.19136456e-02,1.23630092e-01,-3.14735830e-01],[-1.68371245e-01,1.78006962e-01,2.63823152e-01,1.59781501e-01,-2.13619113e-01,4.40176465e-02,2.65233554e-02,3.37381698e-02,1.17388099e-01,4.72911494e-03,4.56971601e-02,1.37098521e-01],[1.17798127e-01,1.67792349e-03,-3.48504409e-02,-3.04003879e-02,-7.37465024e-02,1.43222570e-01,1.58967003e-01,-1.98024124e-01,1.09072812e-01,-1.85857534e-01,-1.49162844e-01,8.53664652e-02],[-8.29409882e-02,-2.49471702e-02,-1.22500680e-01,-3.01464424e-02,-3.77497882e-01,4.20864932e-02,8.45945701e-02,-3.50820959e-01,-2.15124547e-01,-5.98947667e-02,1.92754745e-01,-2.16608033e-01],[-4.88656834e-02,-8.98360237e-02,2.96127528e-01,-1.25442715e-02,-3.66703898e-01,-2.56709278e-01,-1.76681951e-01,-2.15441123e-01,4.23765212e-01,-4.58674207e-02,1.36228576e-01,-2.46410370e-01],[-1.22492097e-01,9.61002409e-02,2.56066233e-01,3.42913747e-01,-3.30265880e-01,-1.26571491e-01,2.76153609e-02,-2.02941671e-01,9.37799644e-03,-2.33571857e-01,-1.02396041e-01,1.44419670e-01],[-2.55303949e-01,1.16298027e-01,-4.12234454e-04,3.17080796e-01,-1.67135209e-01,3.03653739e-02,-7.09446818e-02,3.45578231e-02,1.07397869e-01,1.31035730e-01,-2.17410117e-01,2.76542097e-01],[1.78899273e-01,4.71901707e-02,1.25060782e-01,2.10350603e-01,-1.31303906e-01,-1.80790666e-02,-2.21551210e-01,1.26231253e-01,-2.52228007e-02,-1.37592658e-01,-1.51364923e-01,1.80695891e-01],[2.35004853e-02,-1.59424618e-02,-2.20002890e-01,1.19634852e-01,1.12129919e-01,2.97834635e-01,-9.12526250e-02,1.05429627e-01,-1.85580209e-01,3.26812677e-02,3.20251435e-01,2.50461131e-01],[1.29595131e-01,-8.84615555e-02,-1.11113660e-01,-1.57454103e-01,-1.09496668e-01,2.14140177e-01,-2.34346807e-01,-1.91171691e-01,-3.93662453e-02,-2.24379107e-01,2.21376475e-02,2.27674901e-01],[3.47165585e-01,-1.26540229e-01,-9.03277192e-03,-1.37708923e-02,-1.56030402e-01,1.27270222e-01,-1.20849103e-01,-4.81495401e-03,-8.95270631e-02,-1.84205920e-01,3.11589420e-01,1.85596615e-01],[5.77687807e-02,-7.80865103e-02,1.16449021e-01,-1.20669700e-01,2.34645650e-01,-3.58650237e-02,-8.33989754e-02,-1.31515905e-01,-5.36730662e-02,2.14440435e-01,6.29350021e-02,2.03028336e-01],[3.07422310e-01,-5.93488151e-03,5.77413291e-02,-8.18127617e-02,6.03892431e-02,-2.32369095e-01,1.03739180e-01,1.27250105e-01,1.74949691e-01,3.72929424e-02,5.55226356e-02,1.37014493e-01],[1.17375009e-01,-1.97225198e-01,1.81004047e-01,-4.31087762e-02,1.15530327e-01,2.35820085e-01,-2.44831294e-01,1.77845091e-01,3.92837077e-02,-1.87140435e-01,1.76943049e-01,2.08556533e-01],[-1.31827950e-01,1.24585398e-01,-1.47262454e-01,-1.73512958e-02,-1.85870454e-01,1.40444236e-02,-1.35350421e-01,9.20118019e-03,-4.35135216e-02,-1.15606964e-01,1.61001533e-01,-5.74481525e-02],[-7.46327862e-02,-1.88455075e-01,5.96026555e-02,-1.00426013e-02,1.84031576e-01,6.43741265e-02,-9.47682112e-02,-2.28724033e-01,-5.78862689e-02,1.23691268e-01,1.71810448e-01,-2.54641056e-01],[-1.95918381e-02,2.84675206e-03,-6.10275194e-02,5.48375957e-02,4.84431572e-02,-1.10902525e-02,4.88718674e-02,2.33902991e-01,-9.25870799e-03,8.80988687e-02,1.93984166e-01,-1.10583857e-01],[-7.26860464e-02,-1.31485105e-01,-2.23394990e-01,-3.21135968e-01,-5.01396321e-02,-1.27160355e-01,1.96730599e-01,-1.65078834e-01,-1.28353223e-01,-1.28749311e-02,2.11222276e-01,5.63697927e-02],[1.59015656e-01,-1.89554781e-01,1.73388556e-01,-2.57979911e-02,3.01036257e-02,-8.58168826e-02,7.73473457e-02,-1.69526070e-01,-4.19751601e-03,-1.15612432e-01,7.43914545e-02,-6.13594204e-02],[-1.35318145e-01,-2.41163209e-01,-1.15575261e-01,1.03088155e-01,-2.64600813e-01,3.51843685e-01,-1.41781881e-01,-1.90111950e-01,-2.69476175e-01,-3.69278014e-01,2.64586151e-01,-1.25644684e-01],[-1.34888114e-02,-4.53434438e-02,2.84672111e-01,1.25705734e-01,2.46516708e-02,5.96589781e-02,-7.49945119e-02,-1.50127798e-01,-1.31756112e-01,-5.20046148e-03,-1.14536867e-01,-7.65101016e-02],[1.04763448e-01,1.98703885e-01,-3.73305194e-02,5.11175022e-02,2.52579385e-03,1.05722949e-01,-1.76787376e-01,-1.50903866e-01,-5.74791618e-02,6.70620846e-03,-2.76997596e-01,-1.83977440e-01],[-1.21760421e-01,-5.12502827e-02,-2.44486079e-01,-1.38744831e-01,-1.62022591e-01,2.61078384e-02,1.97061896e-01,-1.38672695e-01,-1.21544227e-01,1.11699417e-01,-2.94709861e-01,9.56392214e-02],[7.35251456e-02,1.62510760e-02,4.20932695e-02,1.78703025e-01,2.16191396e-01,-7.63951689e-02,-1.34583727e-01,1.00354567e-01,8.97847414e-02,-1.00793010e-02,1.46123739e-02,1.22234233e-01],[1.50285378e-01,2.66131759e-01,-2.64949501e-01,7.16419592e-02,-6.56904876e-02,1.13791041e-01,-3.82739216e-01,3.81933242e-01,-1.42667428e-01,2.08126288e-02,-7.09077492e-02,6.66025728e-02],[1.35233179e-01,2.06389222e-02,1.69254884e-01,-5.26923053e-02,3.22288424e-01,-3.17601301e-02,-5.57804666e-02,2.23181129e-01,7.10840374e-02,1.84861973e-01,-3.14896703e-02,-2.91519985e-02],[1.74970329e-01,-1.10573404e-01,4.26120497e-02,-9.19493660e-02,-1.84233487e-02,3.76622118e-02,-7.90851191e-03,7.31965601e-02,-1.34988338e-01,-9.94593576e-02,3.36214267e-02,1.35469630e-01],[1.94806710e-01,-7.00211152e-02,-1.01034038e-01,-1.85382336e-01,-8.89801458e-02,1.07769810e-01,3.74038331e-02,-5.85109740e-02,-5.47550712e-03,8.75202939e-02,5.23663759e-02,2.00835004e-01],[1.06442884e-01,-5.50026484e-02,-1.72790706e-01,-7.43817613e-02,-5.73304966e-02,-1.52986929e-01,2.29224227e-02,6.26656339e-02,1.63729206e-01,-5.36044724e-02,-7.29588494e-02,1.70297638e-01],[-8.41791034e-02,-2.62017369e-01,1.22105412e-01,1.82551399e-01,1.76745459e-01,1.33476034e-01,-8.28775167e-02,4.65711392e-02,-4.37372327e-02,-1.09076612e-02,-1.03825536e-02,1.57469496e-01],[2.63230622e-01,-1.47552326e-01,-9.75049809e-02,-4.87323441e-02,1.59223974e-01,1.09313875e-01,1.82954744e-02,-1.35725871e-01,2.57787436e-01,4.34942581e-02,-8.94831046e-02,-2.20811129e-01],[6.60300702e-02,5.83675243e-02,2.49803811e-02,1.06528988e-02,-2.32538149e-01,7.92545006e-02,1.49402663e-01,1.21036358e-01,-1.43704757e-01,3.75723541e-02,-5.48053160e-02,-1.22583389e-01],[5.00300825e-02,2.23506972e-01,1.12249278e-01,2.07158506e-01,-7.94694424e-02,4.57523838e-02,-3.50405797e-02,2.17014134e-01,3.74063812e-02,6.81494474e-02,-3.39535363e-02,-1.21481828e-01],[1.82995096e-01,2.84170330e-01,-5.23368502e-03,1.08113781e-01,2.22278640e-01,-1.47102371e-01,6.03073910e-02,9.75212008e-02,-7.31717870e-02,1.14418827e-02,6.99812546e-02,8.65542442e-02],[-1.48003073e-02,1.33675322e-01,-1.53416991e-01,-1.48183092e-01,1.47773758e-01,2.19915640e-02,-1.08821623e-01,9.50391591e-02,-4.58755232e-02,1.90433249e-01,-8.54239911e-02,7.73122832e-02]],dtype=np.float)
	b0=np.array([0.22709577,0.19766952,0.01995138,-0.04603582,0.01704955,0.01437583,0.05359448,-0.02731087,0.21360077,-0.07868154,-0.07776031,-0.16930926],dtype=np.float)
	z1=np.dot(input_data,w0)+b0
	a1=_relu(z1)
	return a1
def _layer_one(input):
	w1=np.array([[-1.0203481,0.46559307,-0.90648866,0.38084486,0.63899696,-0.9992195,0.8293284,0.27000228],[-0.2910284,-0.52721786,-0.40077013,0.16102973,0.7513776,-0.9326905,0.8123616,0.9563922],[0.76624835,0.48214787,0.81875545,-0.6023574,-0.02267493,0.5544211,-0.63002443,-0.41798884],[0.14604479,-0.23465909,0.34627366,-0.56753683,-0.8076582,0.16675556,-0.27811536,-0.36773536],[0.70223564,0.40773264,0.7151527,-0.53273094,-0.7913494,0.7881167,-0.3787351,-0.43144867],[-0.03614731,0.21656777,-0.759399,0.42939952,0.06886981,-0.60933244,-0.49799868,0.15505937],[0.02860112,0.43704703,-0.672733,-0.43158615,0.8740345,0.20003332,0.45194054,0.3210791],[0.15656586,0.26368082,-0.1948867,-0.26360726,-0.36085114,0.3431014,-0.29323974,0.42509705],[0.09939747,-0.20705642,0.51196814,0.05691895,0.34692687,0.49042138,0.41174233,0.2256699],[0.32137677,-0.87251765,-0.0379138,-0.08180265,-0.00335148,0.5709534,-0.5237682,-0.57087135],[-0.8040256,0.1928722,0.11546769,0.16279563,0.856959,-0.63919276,0.34508547,0.32145658],[-0.528815,-0.31074256,-0.04968386,0.32441455,-0.7268404,-0.2714887,-0.4780787,-0.3288983]],dtype=np.float)
	b1=np.array([0.14329214,0.02244809,0.07480378,-0.00108605,0.10871821,0.00806387,0.11875808,0.0619337],dtype=np.float)
	z2=np.dot(input,w1)+b1
	a2=_relu(z2)
	return a2
def _layer_three(input):
	w2=np.array([[0.48954403],[-1.2882802],[0.7204739],[0.31496158],[-1.4293383],[1.2237549],[-1.4405941],[-1.1687659]],dtype=np.float)
	b2=np.array([-0.07027833],dtype=np.float)
	z3=np.dot(input,w2)+b2
	return _sigmoid(z3)
def predict(input_data):
	a=_layer_zero(input_data)
	b=_layer_one(a)
	return _layer_three(b)