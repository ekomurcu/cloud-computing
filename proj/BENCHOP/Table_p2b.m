%% Problem 1 b) II

function [timeBSamPutUII,relerrBSamPutUII] = Table_p2b()
Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};
display('Problem 1 b) II');
rootpath=pwd;
S=[97,98,99]; K=100; T=0.25; r=0.1; sig=0.01;
U=[3.000000000000682 2.000000000010786   1.000000000010715];

filepathsBSamPutUII=getfilenames('./','BSamPutUII_*.m');
par={S,K,T,r,sig};
[timeBSamPutUII,relerrBSamPutUII] = executor(rootpath,filepathsBSamPutUII,U,par);

tBSamPutUII=NaN(numel(Methods),1); rBSamPutUII=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSamPutUII)
        a=filepathsBSamPutUII{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSamPutUII(ii)=timeBSamPutUII(jj);
            rBSamPutUII(ii)=relerrBSamPutUII(jj);
        end
    end
end

cd(rootpath);
