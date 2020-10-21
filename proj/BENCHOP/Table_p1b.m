%% Problem 1 b) I

function [timeBSamPutUI,relerrBSamPutUI] = Table_p1b()
Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};
display('Problem 1 b) I');
rootpath=pwd;
S=[90,100,110]; K=100; T=1.0; r=0.03; sig=0.15;
U=[10.726486710094511 4.820608184813253 1.828207584020458];

filepathsBSamPutUI=getfilenames('./','BSamPutUI_*.m');
par={S,K,T,r,sig};
[timeBSamPutUI,relerrBSamPutUI] = executor(rootpath,filepathsBSamPutUI,U,par);

tBSamPutUI=NaN(numel(Methods),1); rBSamPutUI=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSamPutUI)
        a=filepathsBSamPutUI{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSamPutUI(ii)=timeBSamPutUI(jj);
            rBSamPutUI(ii)=relerrBSamPutUI(jj);
        end
    end
end

cd(rootpath);
