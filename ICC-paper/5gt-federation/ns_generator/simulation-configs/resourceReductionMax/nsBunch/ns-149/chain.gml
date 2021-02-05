graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 8
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 2
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 147
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 117
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 78
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 84
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 117
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 164
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 125
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 156
  ]
]
