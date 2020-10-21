
%% Problem 1 c) I

function [timeBSupoutCallI,relerrBSupoutCallI] = Table_p1c()
Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};
display('Problem 1 c) I');
rootpath=pwd;
S=[90,100,110]; K=100; T=1.0; r=0.03; sig=0.15; B=1.25*K;
U=[1.822512255945242 3.294086516281595 3.221591131246868];

filepathsBSupoutCallI=getfilenames('./','BSupoutCallI_*.m');
par={S,K,T,r,sig,B};
[timeBSupoutCallI,relerrBSupoutCallI] = executor(rootpath,filepathsBSupoutCallI,U,par);

tBSupoutCallI=NaN(numel(Methods),1); rBSupoutCallI=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSupoutCallI)
        a=filepathsBSupoutCallI{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSupoutCallI(ii)=timeBSupoutCallI(jj);
            rBSupoutCallI(ii)=relerrBSupoutCallI(jj);
        end
    end
end

cd(rootpath);
