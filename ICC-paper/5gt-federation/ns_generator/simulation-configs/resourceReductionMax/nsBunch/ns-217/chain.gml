graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 2
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 4
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 2
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 3
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
    delay 35
    bw 126
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 81
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 120
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 70
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 81
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 108
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 151
  ]
]
