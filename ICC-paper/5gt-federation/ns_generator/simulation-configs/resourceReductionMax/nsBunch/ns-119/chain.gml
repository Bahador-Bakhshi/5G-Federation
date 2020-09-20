graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 184
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 53
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 101
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 74
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 147
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 143
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 151
  ]
]
