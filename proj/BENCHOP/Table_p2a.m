%% Problem 1 a) II

function [timeBSeuCallUII,relerrBSeuCallUII] = Table_p2a()
Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};
display('Problem 1 a) II');
rootpath=pwd;
S=[97,98,99]; sig=0.01; r=0.1; T=0.25; K=100;
U=[0.033913177006141   0.512978189232598   1.469203342553328];

filepathsBSeuCallUII=getfilenames('./','BSeuCallUII_*.m');
par={S,K,T,r,sig};
[timeBSeuCallUII,relerrBSeuCallUII] = executor(rootpath,filepathsBSeuCallUII,U,par);

tBSeuCallUII=NaN(numel(Methods),1); rBSeuCallUII=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSeuCallUII)
        a=filepathsBSeuCallUII{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSeuCallUII(ii)=timeBSeuCallUII(jj);
            rBSeuCallUII(ii)=relerrBSeuCallUII(jj);
        end
    end
end

cd(rootpath);
