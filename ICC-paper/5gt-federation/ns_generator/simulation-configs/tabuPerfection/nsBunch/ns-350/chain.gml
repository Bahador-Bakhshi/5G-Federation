graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 9
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 3
    memory 12
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 106
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 92
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 132
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 186
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 65
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 175
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 105
  ]
]
