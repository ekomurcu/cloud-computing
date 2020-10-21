%% Problem 1 c) II

function [timeBSupoutCallII,relerrBSupoutCallII] = Table_p2c()
Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};
display('Problem 1 c) II');
rootpath=pwd;
S=[97,98,99]; sig=0.01; r=0.1; T=0.25; K=100; B=1.25*K;
U=[0.033913177006134   0.512978189232598   1.469203342553328];

filepathsBSupoutCallII=getfilenames('./','BSupoutCallII_*.m');
par={S,K,T,r,sig,B};
[timeBSupoutCallII,relerrBSupoutCallII] = executor(rootpath,filepathsBSupoutCallII,U,par);

tBSupoutCallII=NaN(numel(Methods),1); rBSupoutCallII=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSupoutCallII)
        a=filepathsBSupoutCallII{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSupoutCallII(ii)=timeBSupoutCallII(jj);
            rBSupoutCallII(ii)=relerrBSupoutCallII(jj);
        end
    end
end

cd(rootpath);
