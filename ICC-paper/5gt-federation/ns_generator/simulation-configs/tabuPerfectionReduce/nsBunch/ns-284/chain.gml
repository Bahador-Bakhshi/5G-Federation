graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 95
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 60
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 198
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 83
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 51
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 134
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 62
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 84
  ]
]
