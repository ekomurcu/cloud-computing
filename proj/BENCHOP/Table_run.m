function [time,relerr] = Table_run(problem)

  format long

  warning on

  Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
           'FFT','FGL','COS',...
           'FD','FD-NU','FD-AD',...
           'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};

  if problem == 1
    [time, relerr] = Table_p1a();
  elseif problem == 2
    [time, relerr] = Table_p1b();
  elseif problem == 3
    [time, relerr] = Table_p1c();
  elseif problem == 4
    [time, relerr] = Table_p2a();
  elseif problem == 5
    [time, relerr] = Table_p2b();
  elseif problem == 6_
    [time, relerr] = Table_p2c();
  end
end
