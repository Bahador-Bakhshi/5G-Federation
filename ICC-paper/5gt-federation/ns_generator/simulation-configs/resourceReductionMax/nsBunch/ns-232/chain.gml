graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 11
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 1
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 84
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 118
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 84
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 149
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 75
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 51
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 84
  ]
]
