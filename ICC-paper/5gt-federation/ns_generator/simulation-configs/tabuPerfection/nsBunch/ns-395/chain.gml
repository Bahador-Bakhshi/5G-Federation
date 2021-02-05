graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 4
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 110
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 163
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 148
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 78
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 113
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 104
  ]
]
