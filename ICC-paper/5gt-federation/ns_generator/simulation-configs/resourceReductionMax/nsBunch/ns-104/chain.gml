graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 9
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 9
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 16
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 12
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 92
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 65
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 110
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 181
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 85
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 89
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 71
  ]
]
