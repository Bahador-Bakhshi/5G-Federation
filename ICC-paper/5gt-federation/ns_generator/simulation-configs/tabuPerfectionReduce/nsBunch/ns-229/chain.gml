graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 12
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 127
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 61
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 105
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 147
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 122
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 110
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 90
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 199
  ]
]
